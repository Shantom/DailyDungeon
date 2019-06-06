# -*- coding: utf-8 -*-

# This is a High Low Guess game Alexa Skill.
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.
import random
import logging
import time
from collections import defaultdict

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
from alexa.character import Character

tree = lambda: defaultdict(tree)

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
    session_attr = tree()
    
    if not attr:
        session_attr['game_state'] = "WAIT_FOR_CREATION"

        speech_text = (
            "Welcome to Daily Dungeon. I don’t think I have any of your characters here. "
            "Would you like to create one?")
        reprompt = "Would you like to create a new character?"

        attr = tree()
        attr['default_char'] = 0
        attr['characters']['0'] = Character()

        handler_input.attributes_manager.persistent_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()

        handler_input.response_builder.speak(speech_text).ask(reprompt)
    else:

        speech_text = (
            "Welcome to Daily Dungeon."
            "Logging into your character of level-9 and Dungeon of floor-4. ")
        reprompt = "Would you like to create a new character?"

        handler_input.response_builder.speak(speech_text).ask(reprompt)

    handler_input.attributes_manager.session_attributes = session_attr

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("BossInfoIntent"))
def hello_world_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    speech_text = "Baphomet is a legendary notorious demon that lives in the deep jungle. "
    
    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for Help Intent."""
    speech_text = (
        "I am thinking of a number between zero and one hundred, try to "
        "guess it and I will tell you if you got it or it is higher or "
        "lower")
    reprompt = "Try saying a number."

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
    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response

def currently_playing(handler_input):
    # type: (HandlerInput) -> bool
    """Function that acts as can handle for game state."""
    is_currently_playing = False
    session_attr = handler_input.attributes_manager.session_attributes

    if ("game_state" in session_attr
            and session_attr['game_state'] == "STARTED"):
        is_currently_playing = True

    return is_currently_playing

@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.YesIntent")(input))
def yes_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "STARTED"
    session_attr['guess_number'] = random.randint(0, 3)
    session_attr['no_of_guesses'] = 0

    speech_text = "Great! Try saying a number to start the game."
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.NoIntent")(input))
def no_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for No Intent, only if the player said no for
    a new game.
    """
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "ENDED"
    session_attr['ended_session_count'] += 1

    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speech_text = "Ok. See you next time!!"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=lambda input:
                    currently_playing(input) and
                    is_intent_name("NumberGuessIntent")(input))
def number_guess_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for processing guess with target."""
    session_attr = handler_input.attributes_manager.session_attributes
    target_num = session_attr["guess_number"]
    guess_num = int(handler_input.request_envelope.request.intent.slots[
        "number"].value)

    session_attr["no_of_guesses"] += 1

    if guess_num > target_num:
        speech_text = (
            "{} is too high. Try saying a smaller number.".format(guess_num))
        reprompt = "Try saying a smaller number."
    elif guess_num < target_num:
        speech_text = (
            "{} is too low. Try saying a larger number.".format(guess_num))
        reprompt = "Try saying a larger number."
    elif guess_num == target_num:
        speech_text = (
            "Congratulations. {} is the correct guess. "
            "You guessed the number in {} guesses. "
            "Would you like to play a new game?".format(
                guess_num, session_attr["no_of_guesses"]))
        reprompt = "Say yes to start a new game or no to end the game"
        session_attr["games_played"] += 1
        session_attr["game_state"] = "ENDED"

        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
    else:
        speech_text = "Sorry, I didn't get that. Try saying a number."
        reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response

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

    if ("game_state" in session_attr and
            session_attr["game_state"]=="STARTED"):
        speech_text = (
            "The {} skill can't help you with that.".format(SKILL_NAME))
        # reprompt = "Please guess a number between 0 and 100."
    else:
        speech_text = (
            "The {} skill can't help you with that.".format(SKILL_NAME))
        # reprompt = "Say yes to start the game or no to quit."

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    """Handler for all other unhandled requests."""
    speech = "Say yes to continue or no to end the game!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response

@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # type: (HandlerInput, Exception) -> Response
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    logger.error(exception, exc_info=True)
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response

@sb.global_response_interceptor()
def log_response(handler_input, response):
    # type: (HandlerInput, Response) -> None
    """Response logger."""
    logger.info("Response: {}".format(response))


handler = sb.lambda_handler()
