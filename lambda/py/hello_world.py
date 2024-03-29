# -*- coding: utf-8 -*-

# This is a High Low Guess game Alexa Skill.
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.
from html.parser import HTMLParser
import random
import logging
import time
import datetime
import uuid
import json
from collections import defaultdict
import re

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name, get_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.response_helper import get_plain_text_content, get_rich_text_content
from ask_sdk_model.interfaces.display import (
    ImageInstance, Image, RenderTemplateDirective, ListTemplate1,
    BackButtonBehavior, ListItem, BodyTemplate2)
from ask_sdk_model import ui

from ask_sdk_model import Response
from alexa.character import Character, TempCharacter
from alexa.maze import Maze, Room
from alexa import data


def tree(): return defaultdict(tree)


SKILL_NAME = 'Daily Dungeon Game'
sb = StandardSkillBuilder(table_name="DailyDungeon", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for Skill Launch.
    """
    attr = handler_input.attributes_manager.persistent_attributes
    speech_text = ''

    if not attr:
        # create a new one
        attr['character'] = Character().to_dict()
        handler_input.attributes_manager.persistent_attributes = attr

        speech_text += (
            "Welcome to Daily Dungeon. "
            "Seems you don't have a character here, so I just created one for you. ")

        card_text='Character created successfully.'

    else:
        # load the char and claim trophy

        attr = handler_input.attributes_manager.persistent_attributes
        cur_char = Character(attr['character'])
        passing_time, loot_exp = cur_char.claim_loot()
        speech_text = 'Welcome to Daily Dungeon. '
        day = passing_time // (24 * 3600)
        hour = (passing_time % (24 * 3600)) // 3600
        minute = (passing_time % 3600) // 60
        if day > 1:
            speech_time = '{} days and {} hours'.format(day, hour)
        elif day == 1:
            speech_time = 'one day and {} hours'.format(hour)
        elif hour > 1:
            speech_time = '{} hours and {} minutes'.format(hour, minute)
        elif hour == 1:
            speech_time = 'one hour and {} minutes'.format(minute)
        else:
            speech_time = '{} minutes'.format(minute)

        speech_text += 'It\'s been ' + speech_time + ' since your last login. '

        card_text = 'Offline time: ' + str(datetime.timedelta(seconds=passing_time)) + '\nExp obtained:{} \n'.format(loot_exp)

        if cur_char.messages:
            speech_text += 'You have unread messages. '
            card_text += 'You have unread messages. \n'

        attr['character'] = cur_char.to_dict()

    if 'in_maze' in attr and (attr['in_maze'] == 'IN' or attr['in_maze'] == 'WAIT'):
        speech_text += 'You didnt finish your maze. Say resume the maze to go back to where you were. '
        card_text += 'You did not finish your maze. '
        attr['in_maze'] = 'WAIT'

    card = ui.SimpleCard(
        title='Welcome to Daily Dungeon',
        content=card_text
    )

    handler_input.attributes_manager.save_persistent_attributes()

    handler_input.response_builder.speak(
        speech_text).ask('what would you like to do').set_card(card)

    return handler_input.response_builder.response

def YTDurationToSeconds(duration):
    def _js_parseInt(string):
        return int(''.join([x for x in string if x.isdigit()]))
    match = re.match('PT(\d+H)?(\d+M)?(\d+S)?', duration).groups()
    hours = _js_parseInt(match[0]) if match[0] else 0
    minutes = _js_parseInt(match[1]) if match[1] else 0
    seconds = _js_parseInt(match[2]) if match[2] else 0
    return hours * 3600 + minutes * 60 + seconds

@sb.request_handler(can_handle_func=is_intent_name("FarmIntent"))
def farm_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])

    duration = get_slot_value(handler_input, 'duration')
    if not duration.startswith('PT'):
        duration = 'PT24H'
    duration=YTDurationToSeconds(duration)
    _, loot_exp = cur_char.claim_loot(duration)

    speech_text = 'You got {} experience points. '.format(loot_exp)

    card_text = 'Farm time: ' + str(datetime.timedelta(seconds=duration)) + '\nExp obtained:{} \n'.format(loot_exp)

    if cur_char.messages:
        speech_text += 'You have unread messages. '
        card_text += 'You have unread messages. \n'

    attr['character'] = cur_char.to_dict()
    
    card = ui.SimpleCard(
        title='Farm Result (Debug Only)',
        content=card_text
    )

    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_card(card).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("CheckMessagesIntent"))
def check_messages_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])
    speech_text = ""
    if not cur_char.messages:
        speech_text += "You have no message."
    else:
        speech_text += cur_char.messages.pop(0)
        speech_text += ' {} messages left. '.format(len(cur_char.messages))

    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("EnterMazeIntent")(input)
                    and is_in_maze(input) == 'NO')
def enter_maze_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    attr['in_maze'] = 'IN'
    cur_char = Character(attr['character'])
    floor = cur_char.floor
    maze = Maze(floor=floor)
    attr['maze'] = maze.to_dict()

    attr['temp_buff'] = TempCharacter().to_dict()

    speech_text = "You entered the maze. You are currently in room-{}. Now pick up a direction and move.".format(
        maze.cur_room.id)

    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("ResumeMazeIntent")(input)
                    and is_in_maze(input) == 'WAIT')
def resume_maze_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    attr['in_maze'] = 'IN'

    speech_text = 'You returned to the maze. Say where am I to locate yourself. '

    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("DiscardMazeIntent")(input)
                    and is_in_maze(input) != 'NO')
def discard_maze_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    attr['in_maze'] = 'NO'

    speech_text = 'The maze has been discarded. '

    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("LocationIntent")(input)
                    and is_in_maze(input) == 'IN')
def location_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    maze = Maze(maze_data=attr['maze'])
    cur_id = maze.cur_room.id
    speech_text = "You are now in room-{}. ".format(cur_id)
    reprompt = 'You have visited every adjacent room. Now pick up a direction. '
    for dir in random.sample(['north', 'south', 'west', 'east'], 4):
        if getattr(maze.cur_room, dir) and not maze.rooms[getattr(maze.cur_room, dir)].is_marked:
            # not visited room
            reprompt = 'You haven\'t visited the room in the ' + dir
            break

    speech_text += reprompt

    handler_input.response_builder.speak(
        speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("MoveIntent")(input)
                    and is_in_maze(input) == 'IN')
def move_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    direction = get_slot_value(handler_input, 'direction')
    if direction not in ['north', 'south', 'west', 'east']:
        handler_input.response_builder.speak(
            'please say a direction').set_should_end_session(False)
        return handler_input.response_builder.response

    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])

    maze = Maze(maze_data=attr['maze'])
    if not getattr(maze.cur_room, direction):  # no way on this direction
        speech_text = "Sorry, there is no way at {}".format(direction)
    else:
        new_room = maze.rooms[getattr(maze.cur_room, direction)]
        room_type = new_room.room_type
        temp_buff = TempCharacter(attr['temp_buff'])
        if room_type == 'BOSS':
            # TODO: fight a boss
            speech_text = 'You finally found the boss room. You can challenge the boss here.'
            attr['ready_for_boss'] = True

            pass
        else:
            speech_text = 'You entered room-{}. '.format(new_room.id)
            speech_text += temp_buff.process(room_type, cur_char)
            attr['temp_buff'] = temp_buff.to_dict()
            attr['ready_for_boss'] = False
            new_room.mark()

        maze.cur_room = new_room

    attr['maze'] = maze.to_dict()
    handler_input.attributes_manager.save_persistent_attributes()
    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("ChallengeBossIntent")(input)
                    and is_in_maze(input) == 'IN'
                    and ready_for_boss(input))
def challenge_boss_intent_handler(handler_input):
    # type: (HandlerInput) -> Response

    attr = handler_input.attributes_manager.persistent_attributes
    session_attr = handler_input.attributes_manager.session_attributes

    cur_char = Character(attr['character'])
    temp_buff = TempCharacter(attr['temp_buff'])
    is_win, log_battle, log_vec = cur_char.battle_with_boss(temp_buff)
    session_attr['last_battle_log'] = log_battle
    session_attr['last_battle_log_vec'] = log_vec

    if is_win:
        speech_text = "You passed the challenge, welcome to floor-{}".format(
            cur_char.floor)
        attr['in_maze'] = 'NO'
        attr['ready_for_boss'] = False
    else:
        speech_text = 'Sorry but you failed to beat the boss. Say review last battle to prepare next try'

    attr['character'] = cur_char.to_dict()
    handler_input.attributes_manager.save_persistent_attributes()

    handler_input.response_builder.speak(
        speech_text).ask('Do you need the battle info')
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("BattleLogIntent"))
def battle_log_intent_handler(handler_input):
    # type: (HandlerInput) -> Response

    session_attr = handler_input.attributes_manager.session_attributes
    if 'last_battle_log' in session_attr.keys():
        speech_text = '.\n'.join(session_attr['last_battle_log'])
        logger.info('Telling battle info.' + speech_text)

        if supports_display(handler_input):
            item_list = session_attr['last_battle_log_vec'] 
            handler_input.response_builder.add_directive(
                RenderTemplateDirective(
                    ListTemplate1(
                        title='Battle Review',
                        list_items=item_list
                    )))

    else:
        speech_text = 'Seems you don\'t have a battle.'
        logger.info('No battle info.')

    # TODO: set a readable card here

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)

    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("BossInfoIntent"))
def boss_info_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    query = get_slot_value(handler_input, 'bossname')
    if not query:
        attr = handler_input.attributes_manager.persistent_attributes
        cur_char = Character(attr['character'])
        query = data.BOSS_OF_FLOOR[cur_char.floor - 1]

    logger.info('query:'+query)

    if query and query in data.MOB_INFO:
        info = data.MOB_INFO[query]
        speech_text = 'Boss {}. It has attack of {}, defense of {}, and HP of {}. '.format(
            query.title(), info['attack'], info['defense'], info['hp'])
        if len(info['skill']):
            speech_text += 'Also, it can use {}'.format(info['skill'])

        title = 'Boss Info: ' + query.title()
        text = 'HP: {} \nAttack: {} Defense: {}\n Agility: {} Dexterity: {}'.format(
            info['hp'], info['attack'], info['defense'], info['speed'], info['cast_speed'])
        if len(info['skill']):
            text += '\n Skill: {}'.format(info['skill'])
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title=title,
                text=text,
                image=ui.Image(
                    small_image_url=data.MONSTER_AVATAR[query],
                    large_image_url=data.MONSTER_AVATAR[query]
                )))

        if supports_display(handler_input):
            img = Image(sources=[ImageInstance(
                url=data.MONSTER_AVATAR[query])])
            primary_text = 'HP: {} <br/>Attack: {} <br/>Defense: {}<br/> Agility: {} <br/>Dexterity: {}'.format(
                info['hp'], info['attack'], info['defense'], info['speed'], info['cast_speed'])
            if len(info['skill']):
                primary_text += '<br/> Skill: {}'.format(info['skill'])
            primary_text = get_rich_text_content(primary_text)
            handler_input.response_builder.add_directive(
                RenderTemplateDirective(
                    BodyTemplate2(
                        back_button=BackButtonBehavior.VISIBLE,
                        image=img, title=title,
                        text_content=primary_text)))
    else:
        speech_text = "You can ask me the current floor's boss or any boss with a name "

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("CheckStatusIntent"))
def check_status_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])
    speech_text = "Your character is level-{} and on floor-{}. ".format(
        cur_char.level, cur_char.floor)
    speech_text += 'He has attack of {} and defense of {}. '.format(
        cur_char.attack, cur_char.defense)

    card =ui.StandardCard(
                title='Character Status',
                text='\tLevel: {}    Floor: {}\nHP: {}    MP: {}\nAttack: {}    Defense: {}\nAgility: {}    Dexterity: {}\nCurrent Skill: {}'.format(cur_char.level, cur_char.floor, cur_char.hp, cur_char.mp, cur_char.attack, cur_char.defense, cur_char.speed, cur_char.cast_speed,cur_char.cur_skill),
                image=ui.Image(
                    small_image_url=data.PLAYER_STANDING,
                    large_image_url=data.PLAYER_STANDING
                ))


    handler_input.response_builder.speak(
        speech_text).set_card(card).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("ChangeSkillsIntent"))
def change_skill_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])

    skill = get_slot_value(handler_input, 'skill').title()

    if skill not in cur_char.skills:
        speech_text = "You don\'t have {} . ".format(skill)
    else:
        cur_char.cur_skill = skill
        speech_text = 'Changed your skill to {}. '.format(skill)

    attr['character'] = cur_char.to_dict()
    handler_input.attributes_manager.save_persistent_attributes()

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("SkillsInfoIntent"))
def skill_info_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    query = get_slot_value(handler_input, 'skill')
    if not query:
        speech_text = "You can ask me a skill with a name. "

    elif query.title() in data.SKILL_INFO:
        info = data.SKILL_INFO[query.title()]
        speech_text = '{} has damage rate of {}. It needs {} time units to cast, and costs {} MP. '.format(
            query.title(), info['rate'], info['cast'], info['mp'])

        title = 'Skill Info: ' + query.title()
        text = 'Damage Rate: {}\n Cast Time: {}\n MP cost: {}'.format(
            info['rate'], info['cast'], info['mp'])
        if info['effect']:
            speech_text += 'Also, it can make the enemy into {}'.format(
                info['effect'])
            text += '\n Effect: {}'.format(info['effect'])

        handler_input.response_builder.set_card(
            ui.StandardCard(
                title=title,
                text=text,
                image=ui.Image(
                    small_image_url=data.MONSTER_AVATAR['?'],
                    large_image_url=data.MONSTER_AVATAR['?']
                )))

        if supports_display(handler_input):
            img = Image(sources=[ImageInstance(
                url=data.MONSTER_AVATAR['?'])])
            primary_text = 'Damage Rate: {}<br/> Cast Time: {} MP cost: {}'.format(
                info['rate'], info['cast'], info['mp'])
            if info['effect']:
                primary_text += '<br/> Effect: {}'.format(info['effect'])
            primary_text = get_rich_text_content(primary_text)
            handler_input.response_builder.add_directive(
                RenderTemplateDirective(
                    BodyTemplate2(
                        back_button=BackButtonBehavior.VISIBLE,
                        image=img, title=title,
                        text_content=primary_text)))

    else:
        speech_text = '{} is not a skill. '.format(query.title())

    logger.info('query:'+query)

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("CheckSkillsIntent"))
def check_skill_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    cur_char = Character(attr['character'])
    speech_text = 'You have {} equipped. '.format(
        cur_char.cur_skill)+"Your current skill set includes {}. ".format(','.join(cur_char.skills))

    card = ui.SimpleCard(title='Character Skills', content='Equipped: {} '.format(
        cur_char.cur_skill)+'List:\n {}\n'.format('\n'.join(cur_char.skills)))

    handler_input.response_builder.speak(speech_text).set_card(
        card).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for Help Intent."""
    # TODO: set a speech here
    speech_text = (
        "Here should be a help speech.")
    reprompt = "Here should be a help reprompt."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Single handler for Cancel and Stop Intent."""
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for Session End."""

    speech_text = "The session ended."
    handler_input.response_builder.speak(speech_text)

    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response


def is_in_maze(handler_input):
    # type: (HandlerInput) -> bool
    """Function that checks if in maze."""
    attr = handler_input.attributes_manager.persistent_attributes
    in_maze = 'NO'
    if 'in_maze' in attr:
        in_maze = attr['in_maze']

    return in_maze


def ready_for_boss(handler_input):
    # type: (HandlerInput) -> bool
    """Function that checks if in maze."""
    attr = handler_input.attributes_manager.persistent_attributes
    ready = False
    if 'ready_for_boss' in attr:
        ready = attr['ready_for_boss']

    return ready


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("AMAZON.FallbackIntent")(input) or
                    is_intent_name("AMAZON.YesIntent")(input) or
                    is_intent_name("AMAZON.NoIntent")(input))
def fallback_handler(handler_input):
    # type: (HandlerInput) -> Response
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    session_attr = handler_input.attributes_manager.session_attributes

    speech_text = (
        "The {} skill can't help you with that.".format(SKILL_NAME))

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for all other unhandled requests."""
    intent_name = get_intent_name(handler_input)
    if intent_name == 'ChallengeBossIntent':
        speech_text = 'You need to be in the boss room to challenge the boss. '
    elif intent_name == 'EnterMazeIntent':
        speech_text = 'You already have a maze in progress. Would you like to resume the maze or discard the maze? '
    elif intent_name == 'ResumeMazeIntent' or intent_name == 'DiscardMazeIntent':
        speech_text = 'You are already in a maze or you don\'t have a maze in progress. Say enter the maze or discard the maze. '
    elif intent_name == 'LocationIntent':
        speech_text = 'You need to be in a maze to locate yourself. Say enter the maze or resume the maze. '
    elif intent_name == 'MoveIntent':
        speech_text = 'You need to be in a maze to take a move. Say enter the maze or resume the maze. '
    else:
        speech_text = 'I am not sure what you are saying. '

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(False)
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # type: (HandlerInput, Exception) -> Response
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    logger.error(exception, exc_info=True)
    speech = "Sorry, an exception occurred. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.global_response_interceptor()
def log_response(handler_input, response):
    # type: (HandlerInput, Response) -> None
    """Response logger."""
    logger.info("Response: {}".format(response))


class SSMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.full_str_list = []
        self.strict = False
        self.convert_charrefs = True

    def handle_data(self, d):
        self.full_str_list.append(d)

    def get_data(self):
        return ''.join(self.full_str_list)


def convert_speech_to_text(ssml_speech):
    """convert ssml speech to text, by removing html tags."""
    # type: (str) -> str
    s = SSMLStripper()
    s.feed(ssml_speech)
    return s.get_data()


@sb.global_response_interceptor()
def add_card(handler_input, response):
    """Add a card by translating ssml text to card content."""
    # type: (HandlerInput, Response) -> None
    if response.card:
        return
    response.card = ui.SimpleCard(
        title='Daily Dungeon',
        content=convert_speech_to_text(response.output_speech.ssml)
    )


def supports_display(handler_input):
    # type: (HandlerInput) -> bool
    """Check if display is supported by the skill."""
    try:
        if hasattr(
            handler_input.request_envelope.context.system.device.
                supported_interfaces, 'display'):
            return (
                handler_input.request_envelope.context.system.device.
                supported_interfaces.display is not None)
    except:
        return False


handler = sb.lambda_handler()
