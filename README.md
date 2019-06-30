# The Daily Dungeon Game via Amazon Alexa

## Overview

### Game Name and Running Environment.

Name: Daily Dungeon

Environment: Amazon Alexa

### Game Background and Story

Our hero, Lin, follows his master into the dungeon to explore the secret, but as soon as he enters the dungeon entrance, his master mysteriously disappears. 
At this time, Lin found that the gate of the dungeon had been closed, and a line appeared on the wall: defeat the four holy beasts before you could escape from here. 
The dungeon is divided into 16 floors, each guarded by a boss, and every four floors guarded by a holy beast. Lin needs to find a way through a maze before he could fight the boss.
Everyday, Lin beats monsters on the current floor to gain experience, with which he gets stronger. 
When Lin finally defeated the four beasts and entered the final floor, only to find that his master is the yellow dragon.

### Game Features

Daily Dungeon is a role-playing game. Players can help Lin through the maze, beat a variety of boss with reasonable skill. 
When players is not on-line, that is, not logged in to the game, Lin will automatically beat the monster on the current floor to gain experience. When the experience value meets the amount required by Lin's current level, Lin will automatically level up and get his ability improved. 
When Lin comes to a specific level, he will learn specific skills. Players can help Lin equip a certain skill to deal with different bosses. 
Players can guide Lin through the maze, in which Lin may encounter many different random events that increase or decrease Lin's temporary statistics.

## Game Mechanism

### Terms

- An **experience** point (often abbreviated to **exp** or **XP**) is a unit of measurement used in role-playing
  games (RPGs) to quantify a player character's progression through the game. Characters
  need exps to level up. [^EXP]

- In RPGs, characters start as fairly weak and untrained. When a sufficient amount of experience is obtained, the character "**levels up**", achieving the next stage of character development. Such an event usually increases the character's statistics. [^LVUP]

- A **statistic** (or **stat**) in role-playing games is a piece of data that represents a particular aspect of a fictional character. That piece of data is usually a integer. [^STAT]

- In video games, a **Boss** is a significant computer-controlled enemy. A fight with a boss character is
  commonly referred to as a boss battle or boss fight. [^BOSS]

- **Farming** refers to a gaming tactic where a player performs repetitive actions to gain experience point
  or some form of in-game currency. [^FARM]

- A **Normal Attack** is executed by the player simply striking a foe. [^NA]

- **Skills** in game are abilities that a character have. They are cast to do special attacks.

- In RPGs, the terms **Buff** and **Debuff** are commonly used to describe **status effects**. *Buff* is the term generically used to describe a positive status effect that affects mainly player or enemy statistics, while *debuff* is to describe a negative status effect. [^BUFF]

[^FARM]:https://www.techopedia.com/definition/19278/farming
[^BOSS]:https://en.wikipedia.org/wiki/Boss_(video_gaming)
[^EXP]:https://en.wikipedia.org/wiki/Experience_point
[^LVUP]: https://en.wikipedia.org/wiki/Experience_point
[^STAT]: https://en.wikipedia.org/wiki/Statistic_(role-playing_games)
[^NA]: https://epicbattlefantasy.fandom.com/wiki/Normal_Attack
[^BUFF]: https://en.wikipedia.org/wiki/Status_effect#Buffs



### Rules

1. When the player is not online, Lin will farm automatically by beating the monster constantly on the current floor to gain experience.
2. Players can explore the maze before the battle to acquire different buffs/debuffs. Also, players can decide which skill to use. 

### Maze and Room

The maze consists of several rooms. Each room has access to the next room, which may exist in one or more of the four directions (north, east, south and west). If there is a random event in the room, it will be triggered when Lin enters. Only in the boss room can Lin challenge boss. When Lin successfully beat the boss, he will automatically exit the maze and  go downstairs to the next floor. If Lin fails, there is no punishment and Lin is still at the boss room.

### Combat Systems

This game uses fully automatic combat. Each side, player or monster, has two progress gauges, a normal attack gauge (up to 100 units) and a cast skill gauge (up to 1000 units). For each unit of time, each of the four gauges is increased by 1 unit. When the progress reaches the required value for the attack or skill to be cast, the player / monster will conduct an attack / skill and subtract the corresponding value from the progress gauge after the move.

### Status Attributes Description

**Attack**: Increases of attack to enemies by increasing damage. It is generally an important index to measure the strength and weakness of characters. 

**Defense**: It determines how much damage can be offset each time it is hit. 

**HP**(Hit Point): the amount of health.

**MP**(Magic Point): Points consumed by skills usage. 

**Agility**: Normal attack speed. A normal attack consumes round of (100/agility) amount of normal attack gauge.

**Dexterity**: Skill cast speed. A skill consumes round of (skill_cast/dexterity) action value, where skill_cast is an attribute of a skill.

### Damage Calculation

Normal Attack: Attacker's attack - defender's defense.

Skill: (Attacker's attack - defender's defense) * skill's rate.

Bleeding: If some side is bleeding, he/it will lose 10% of max HP every time he/it normal attacks.

### Controls

Players completely control via voice. Feedbacks include Alexa voice and display, if there is a screen on the device.

## Game Elements

### Roles

Player: Lin, apprentice of the Master. 

Four Holy Beasts: They are the Azure Dragon of the East, the Vermilion Bird of the South, the White Tiger of the West, and the Black Turtle (also called "Black Warrior") of the North.

Yellow Dragon: The master, central guardian.

### Possible Skills

Thump: a high rate attack skill.

Pierce: a higher rate attack skill.

Blade: Bleeding. Lose HP when normal attacking.

Cross Strike: Bleeding. A higher rate than Blade.

Cold Bolt: Frozen. Decrease normal attack speed.

Blizzard: Frozen. A higher rate than Cold Bolt.

### Possible Random Events

Found a sword: It increases Lin's attack.

Fell over: It decreases Lin's attack.

Found a portion: It either gives Lin extra HP or lose some HP.

Found a shield: It increases Lin's defense.

Attacked by a slime: It decreases Lin's defense.

### Possible Bosses

For floor of 1,2,3,5,6,7,9,10,11,13,14,15, the twelve Chinese zodiac signs, rat, ox, tiger, rabbit, dragon, snake, horse, sheep, monkey, rooster, dog and pig, occupy one floor each.

For floor of 4, 8, 12, 16, the Four Holy Beasts, which are the Azure Dragon of the East, the Vermilion Bird of the South, the White Tiger of the West, and the Black Tortoise of the North, guard each floor.

For the last floor, 17, the Yellow Dragon takes the responsibility.

## Development Platform

### Amazon Alexa

This game project is an Amazon Alexa custom skill. Note that the `skill` here is different from the skill in the previous chapter.

To complete a custom skill project, it is necessary to have a structure of models, lambda and skill manifest. For more details, see Chapter [Components](# Components).

#### Skill manifest

The skill manifest is the JSON representation of the skill, and provides Alexa with all of the metadata required. The metadata include publishing information, such as skill name and description, and supported APIs for devices. [^MANI]

[^MANI]:https://developer.amazon.com/docs/smapi/skill-manifest.html

#### Interaction Models

An interaction model is a voice interface through which users interact with the skill. The model is organized by mapping from users' *spoken* input to the *intents* the cloud-based service can handle. [^MODEL]

[^MODEL]: https://developer.amazon.com/docs/custom-skills/create-the-interaction-model-for-your-skill.html

To declare this mapping, the following inputs are supplied:

1. **Intents**: An *intent* represents an action that fulfills a user's spoken request. Intents can optionally have arguments called *slots*. Intents are specified in a JSON structure called the *intent schema*.
2. **Sample utterances**: A set of likely spoken phrases mapped to the intents. This should include as many representative phrases as possible.
3. **Custom slot types**: A representative list of possible values for a slot. Custom slot types are used for lists of items that are not covered by one of Amazon's built-in slot types.
4. **Dialog model** (optional): A structure that identifies the steps for a *multi-turn conversation* between your skill and the user to collect all the information needed to fulfill each intent. This simplifies the code you need to write to ask the user for information.

A skill can have more than one model in different languages. In this skill, I use only one model, en_US. 

Users say a skill's **invocation name** to begin an interaction with a particular custom skill. This skill's invocation name is "Daily Dungeon", users can say: "Open Daily Dungeon" to launch the skill. 

#### Lambda Function

Lambda function in a custom skill for Alexa is a web service that accepts requests from and sends responses to the Alexa service in the cloud. The web service can be written in any programming language, as long as it meets the requirements below. [^WS]

[^WS]:https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-a-web-service.html

1. The service must be accessible over the Internet.
2. The service must accept HTTP requests on port 443.
3. The service must support HTTP over SSL/TLS, using an Amazon-trusted certificate. Your web service's domain name must be in the `Subject Alternative Names` (SANs) section of the certificate. For testing, you can provide a self-signed certificate.
4. The service must verify that incoming requests come from Alexa. 
5. The service must adhere to the Alexa Skills Kit interface.

I build the service using Python with the Alexa Skills Kit (ASK) SDKs for Python to verify that requests to the web service do come from Alexa. Also, I use [AWS Lambda](# AWS Lambda) to host my web service, which will be mentioned later.

The AWS Lambda requires that its handler's name should be the same as the main code file. Assume that I set the handler's name as `main.handler`, then it calls the handler methods defined in `main.py`.

In `main.py`, handlers are defined here, each processing a certain intent or a kind of request. For more details, see Chapter [Module Design](# Module Design).

#### Session

The skill can keep the *skill session* open to conduct a back-and-forth interaction with the user. While the session is open, the user does not need to use the invocation name to talk to the skill. [^S]

[^S]: https://developer.amazon.com/docs/custom-skills/manage-skill-session-and-session-attributes.html

Lifecycle of a skill session [^S]:

1. A skill session begins when a user invokes your skill and Alexa sends your skill a request. The request contains a session object that uses a Boolean value called `new` to indicate that this is a new session.

2. The skill receives the request and returns a response for Alexa to speak to the user.

3. What happens next depends on the value of the `shouldEndSession` parameter in the skill's **response**:

   - `true` – The session ends. Alexa, not the skill, handles any further speech from the user. If the user re-invokes the skill, Alexa creates a new session (that is, go back to step 1).

   - `false` – The session stays open and Alexa opens the microphone to indicate that she expects the user to respond. If the user's response maps to your interaction model, a new intent is sent to the skill and the process goes back to step 2.

     However, if eight seconds elapse without a response from the user, Alexa closes the microphone. If the skill specified a reprompt, Alexa reprompts the user to speak and opens the microphone for eight more seconds. If the user still does not respond, the session normally ends.

     The session may remain open for a few more seconds with the microphone closed if the skill is used on a device with a screen as described in How devices with screens affect the skill session.

     One exception that overrides this: the directives to start the purchase flow for in-skill purchasing automatically end the session, regardless of the `shouldEndSession` value. You need to use persistent storage to resume the skill once the purchase flow completes. 

   - `undefined` (not set or `null`) – The session's behavior depends on the type of Echo device that the user is interacting with and the content of the response. 

For most of my intents, I set the `shouldEndSession`to `false`, because a game should not end just because the user is thinking for a long time.

#### Cards

Interactions between a user and an Alexa device can include **home cards** displayed in the Amazon Alexa App, the companion app available for Fire OS, Android, iOS, and desktop web browsers. An Alexa-enabled device with a screen also displays cards that have been designed for display in the Alexa app.

差一张图

#### Display Templates

A skill developed for Alexa-enabled devices with a screen can also support **display templates**, which are similar to cards and are viewed directly on the screen.

差一张图

### AWS Lambda

The easiest way to build the cloud-based service for a custom Alexa skill is to use AWS Lambda, an Amazon Web Services offering that runs code only when it's needed and scales automatically, so there is no need to provision or continuously run servers.  [^AL]

I upload my code for my Alexa skill to AWS Lambda and it does the rest, executing it in response to Alexa voice interactions and automatically managing the compute resources.

[^AL]: https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html

### Amazon DynamoDB

It is inevitable to have to store attributes for some reasons. We can store them as session attributes, but they would be lost after the session ends. For those attributes that need to be persistent, we need to use a database to store them. Fortunately, the ASK-SDK for Python allows us to get full access to DynamoDB. 

Amazon DynamoDB is a fully managed proprietary NoSQL database service that supports key-value and document data structures. [^DDB]

[^DDB]:https://en.wikipedia.org/wiki/Amazon_DynamoDB



## Components 

### Manifest

The following is some key metadata in my manifest, which is actually in JSON format.

- Publishing Information
  - locales/en-US
    - name: "Daily Dungeon"
    - description: "An role playing game with idle game element in it."
    - summary: "Launch the skill"
    - example phrases: ["open daily dungeon"]
  - category: "GAME"
- APIs
  - custom
    - endpoint                            #  where the service locates
      - sourceDir: "lambda/py/lambda_upload"
      - uri: "ask-custom-Demo-default"
    - interfaces : [ "RENDER_TEMPLATE"]                          # it is necessary to display

Publishing Information is to determine how the skill is presented to end users in the skill store or Alexa app. APIs specify required information for all interfaces that a skill supports.

### Interaction Model

The following is some key *intents* and their utterances.

- BossInfoIntent:
  - tell me about the boss
  - tell me about {bossname}
- CheckMessagesIntent
  - read my message
  - check my message
- CheckSkillsIntent
  - check my skills
  - check my abilities
- CheckStatusIntent
  - check my status
- ChangeSkillsIntent
  - change my skill to {skill}
  - set my skill to {skill}
- SkillsInfoIntent
  - tell me about {skill}
  - what is {skill}
- ChallengeBossIntent
  - challenge the boss
  - fight the boss
- BattleLogIntent
  - check my last battle
  - review the last battle
- EnterMazeIntent
  - enter the maze
- ResumeMazeIntent
  - resume the maze
- DiscardMazeIntent
  - discard the maze
- LocationIntent
  - where am i
  - locate myself
  - what is around me
- MoveIntent
  - go {direction}
  - head {direction}
  - move to the {direction}

Those words enclosed in brackets are [*slots*](# Interaction Models), where sample values are included.

- LIST_OF_SKILLS (skill)
- LIST_OF_BOSSES (bossname)
- LIST_OF_DIRECTIONS (direction)

### Persistent data

The following is some attributes that need to be stored persistently.

- character: Map
  - level: Number
  - floor: Number
  - exp: Number
  - attack: Number
  - defense: Number
  - hp: Number
  - mp: Number
  - agility: Number
  - dexterity: Number
  - cur_skill: String
  - skills: List of Strings
  - sec_per_round: Number
  - last_offline_time: Number
  - messages: List of Strings
- in_maze: String
- maze: Map
  - cur_room: Map
    - id: String
    - east: String or Null
    - south: String or Null
    - west: String or Null
    - north: String or Null
    - is_visited: Boolean
    - room_type: String or Null
  - rooms: Maps of id to room
    - ...... same as cur_rooms
- ready_for_boss: Boolean
- temp_buff: Map
  - attack: Number
  - defense:: Number
  - hp: Number
  - mp: Number
  - cur_skill: String or Null
  - agility: Number
  - dexterity: Number

### Intent Handlers

These intent handler methods are in the `hello_world.py` file, which is the lambda function entry.

#### LaunchRequest

A `LaunchRequest` is an object that represents that a user made a request to an Alexa skill, but did not provide a specific intent.

The handler firstly checks whether there are already persistent attributes in the database. If not, it will create a new `Character` and store it in the database. If so, it will load the `Character` and call its `claim_loot` method to claim what the character farms during the offline time. Then, it tells users how long they have been offline and how much EXP they obtained.

Also, the attribute `in_maze` tells if Lin is still in a maze or not, which will help users remember where they were at the end of last conversation with Alexa.

图

#### CheckMessagesIntent

There will be something happening during the offline time, such as skill acquirement. Note that our hero, Lin, will level up when he gets enough EXP during the offline farming. Lin acquires a corresponding new skill when he gets to a certain level. Therefore, we need to acknowledge the player what have been acquired. Such messages will be stored as a persistent attribute, which can be read when the player log in.

The handler load the attribute, read the first one out, and pop it out of the attribute. The handler only reads one at a time of this intent.

#### EnterMazeIntent

The `EnterMazeIntent` is the first part of main content of Daily Dungeon. Players need to enter the maze before they could explore it and finally challenge the boss.

At first, the handler checks `in_maze` to determine if Lin has a uncompleted maze. If so, it will tell the user to resume or discard the maze instead of entering a new one. 

If Lin has not entered any maze on this floor, it will create a `Maze` object, which refers to the hard code in `data.py`, depending on which floor Lin is on.  Also, the handler will create a `TempCharacter` object to store temporary status for oncoming random events. These objects will be stored as persistent attributes. Then it tells the user that Lin is in the initial room and encourages them to move.

#### ResumeMazeIntent

If the session ends before Lin successfully defeats the boss. Then the user need to decide either resume the old one or discard it. If the user resumes it, the handler will change `in_maze` to IN that indicates the user can give orders like move or fight.

#### DiscardMazeIntent

Similar to `ResumeMazeIntent`, `DiscardMazeIntent` is the other choice when Lin is still in the maze but the user does not want to continue. Generally, it happens when the user has triggers too many bad events to fight the boss. Fortunately, we provide this option to allow the player to start it over. The handler change  `in_maze` to NO that indicates there is no more maze in use.

#### MoveIntent

This intent is triggered when the player is trying to move to another room. What the player said should include a specific direction, north, east, south or west. If not, the handler will tell the player to specify one. 

When the handler retrieved the direction, it loads the `Maze`, the current `Room`, the `Character` and the `TempCharacter`. According to the Maze and the current Room, it can find if there is a room at that direction. If not, it tells the user to pick up another direction. 

If there is a room at that direction, it changes the current `Room` to the new one and sets the new room as *visited*. Then it checks the new room's type to see if it has a random event to trigger. If so, it puts the obtained buff or debuff on the `TempCharacter`. The player will be told what has been encountered.

If the new room is the boss room, Lin will be able to fight the boss. The handler sets a boolean persistent attribute `ready_for_boss` to store it.

#### LocationIntent

It is easy to lose their way for players, especially right after resuming a maze with a long time of offline. This can be attributed to the fact that Alexa is not a visual platform. There is no map for a maze, so players need to have a rough image in their mind about the what the maze looks like. We provide `LocationIntent` to help players remember where they are, where they have been and where they have not.

The handler loads the `Maze` and the current `Room`. It traverses the current room's four directions in random order. Then it tells the user the current room's id and the first direction it found not visited.

#### ChallengeBossIntent

The goal of entering a maze is to find the boss and defeat it. When Lin is in the boss room and able to fight the boss, the player can give this intent to let Lin fight. 

The handler firstly checks `ready_for_boss` to ensure Lin is in the boss room. It creates a `Battle` object to manage the whole battle. The `Battle` requires the `Character` and `TempCharacter` and returns the battle result and its log information. For more information, see section [Battle](#Battle). If Lin wins, the handler sets `in_maze` to NO and put Lin into the next floor. The handler stores the battle log as a session attribute for the player to review it later.

#### BattleLogIntent

Players can review the last battle log for next try to fight the boss. With the information, it is easy to see what happened during the battle and so that players have another try with another skill or just wait for Lin to farm and get stronger.

The handler loads the battle log attribute, if any. Then let Alexa read it out. If there is a screen on the device, it will display the details of every move of both sides.

#### ChangeSkillsIntent

It is quite normal when Lin successfully beat the boss of the previous floor but fails on the current floor with the same skill equipped. Therefore, players need to make a choice on which skill to use on a certain boss.

The handler tries to get the slot value of *skill* in users' input. When it obtains the new skill name, the handler set the new skill for the current equipped skill. Then it stores it in the database.

#### BossInfoIntent

Players may want to know better the boss they are going to fight. We provide this intent to help users adjust their tactics before they start a battle.

The handler tries to look for the boss name in users' spoken input. If there is not a boss name in the input, it will by default retrieve Lin's current floor's boss name. Then the handler gets the boss information from `data.py` and put it into a sentence, as well as into a Card or a Display Template, if there is a screen in users' device.

#### SkillsInfoIntent

Similar to `BossInfoIntent`, players may want to know what the skills they have actually do or exact statistics of a certain skill. `SkillsInfoIntent` is the right intent.

The handler retrieves information from `data.py` and then gives it to users with voice and display.

#### CheckStatusIntent

This intent is to tell the player the current statistics of Lin, including attack, defense, hp, mp, level, floor, exp and the current equipped skill.

The handler loads the information from database and then gives it to users with voice and display.

#### CheckSkillsIntent

This intent is to tell the player what skills has Lin learned. Players can pick up a suitable skill for fighting a certain boss after they know the information.

The handler loads the information form database and then gives it to users with voice and display.

### Module Design

#### Character

#### Mob

#### Battle

#### Maze

#### Data

## 数值设计

技能

属性

单位时间收益

boss属性

随机事件

迷宫设计



保证游戏过程平滑

## 游戏基本流程





