# Daily Dungeon, A Voice-Based Role-Playing Game on Amazon Alexa Platform

 

## Introduction

### Game Name and Running Environment.

Name: Daily Dungeon

Environment: Amazon Alexa

### Reasons for Using Alexa

Alexa is not just for scheduling, giving reminders or running smart home. Some of the more fun Alexa skills are games, perfect for game night. Daily Dungeon is such a skill for killing time. It probably will not replace your shelf full of video games, but it can help kill 10 or 20 minutes. It works better if players have a piece of paper and pencil to take some notes. However, it needs some patience because it is hard to prevent Alexa from misunderstanding players' response.

People need a kind of casual role playing game, where there is neither complex game system nor boring and repeating farming. Amazon's Alexa is a good platform for a casual RPG, because complex systems and repeating farming are not compatible with voice-only platform.

Players can enjoy a good dungeon atmosphere without a lot of elements to fill up all of their senses. Daily Dungeon was developed at first when only the Echo and Dot were around, which means players can get through the game only with voice interaction. Then it has now added some features for a screen on the Show or Alexa app for Android or iOS. It is much more friendly with a screen.

### Game Background and Story

Our hero, Lin, follows his master into the dungeon to explore the secret, but as soon as he enters the dungeon entrance, his master mysteriously disappears. At this time, Lin found that the gate of the dungeon had been closed, and a line of words appeared on the wall: Defeat the four holy beasts before you could escape from the dungeon. 

The dungeon is divided into 16 floors, each guarded by a boss, and every four floors guarded by a holy beast. Lin needs to find a way through a maze before he is able to fight the boss. Lin beats monsters on the current floor to gain experience, with which he gets stronger. When Lin finally defeats the four beasts and enters the final floor, he finds that his master is the yellow dragon. 

### Game Features

Daily Dungeon is a role-playing game. Players can help Lin through the maze, beat a variety of boss with reasonable skill. 

When players are not on-line, i.e., not logged in to the game, Lin will automatically beat the monster on the current floor to gain experience. When the experience value meets the amount required by Lin's current level, Lin levels up and gets his statistics improved. 

When Lin comes to a specific level, he will learn specific skills. Players can help Lin equip a certain skill to deal with different bosses. Players can guide Lin through the maze, in which Lin may encounter many different random events that increase or decrease Lin's temporary statistics.

## Game Mechanism

The game mechanism is the basic knowledge players should know before they can have fun playing it. This does not necessarily mean that players will not have fun if they do not know it, but the experience might be affected.

### Terms

- An **experience** point (often abbreviated to **exp** or **XP**) is a unit of measurement used in role-playing games (RPGs) to quantify a player character's progression through the game. Characters need exps to level up. [^EXP]
  
- In RPGs, characters start as fairly weak and untrained, i.e. with low statistics. When a sufficient amount of experience is obtained, the character "**levels up**", achieving the next stage of character development. Such an event usually increases the character's statistics. [^LVUP]

- A **statistic** (or **stat**) in role-playing games is a piece of data that represents a particular aspect of a fictional character. That piece of data is usually a integer. [^STAT]

- In video games, a **Boss** is a significant computer-controlled enemy. A fight with a boss character is
  commonly referred to as a boss battle or boss fight. [^BOSS]

- **Farming** refers to a gaming tactic where a player performs repetitive actions to gain experience point
  or some form of in-game currency. [^FARM]

- A **Normal Attack** is executed by the player simply striking a foe. [^NA]

- **Skills** in games are abilities that a character have. A skill is associated with a special attack.

- In RPGs, the terms **Buff** and **Debuff** are commonly used to describe **status effects**. *Buff* is the term generically used to describe a positive status effect that affects mainly player or enemy statistics, while *debuff* is to describe a negative status effect. [^BUFF]

[^FARM]:https://www.techopedia.com/definition/19278/farming
[^BOSS]:https://en.wikipedia.org/wiki/Boss_(video_gaming)
[^EXP]:https://en.wikipedia.org/wiki/Experience_point
[^LVUP]: https://en.wikipedia.org/wiki/Experience_point
[^STAT]: https://en.wikipedia.org/wiki/Statistic_(role-playing_games)
[^NA]: https://epicbattlefantasy.fandom.com/wiki/Normal_Attack
[^BUFF]: https://en.wikipedia.org/wiki/Status_effect#Buffs



### Rules

1. When the player is not online, Lin will farm by beating the monster constantly on the current floor to gain experience. Intuitively, when the player logs in, the their characters will get a certain amount of EXP, which depends on how long it has been offline.
2. Players can explore the maze before the battle to acquire different buffs/debuffs. Also, players can decide which skill to use. 

### Maze and Room

The maze consists of several rooms. Each room has access to the next room, which may exist in one or more of the four directions (north, east, south and west). If there is a random event in the room, it will be triggered when Lin enters. Only in the boss room can Lin challenge the boss. When Lin successfully beat the boss, he will automatically exit the maze and  go downstairs to the next floor. If Lin fails, there is no punishment and Lin is still at the boss room.

### Combat Systems

This game uses fully automatic combat. Players will not feel the process of a combat. The combat is calculated and ends in a moment. It returns a result after the player gives the order to fight. The rule of a combat is as follows.

Each side, player or monster, has two progress gauges: a normal attack gauge (up to 100 units) and a cast skill gauge (up to 1000 units). For each unit of time, each of the four gauges is increased by 1 unit. When the progress reaches the required value for the attack or skill to be cast, the player / monster will conduct an attack / skill and subtract the corresponding value from the progress gauge after the move.

### Status Attributes Description

**Attack**: Increases of attack to enemies by increasing damage. It is generally an important index to measure the strength and weakness of characters. 

**Defense**: It determines how much damage can be offset each time it is hit. 

**HP**(Hit Point): The amount of health.

**MP**(Magic Point): Points consumed by skills usage. 

**Agility**: Normal attack speed. A normal attack consumes round of (100/agility) amount of normal attack gauge.

**Dexterity**: Skill cast speed. A skill consumes round of (skill_cast/dexterity) cast skill gauge, where skill_cast is an attribute of a skill.

### Damage Calculation

Normal Attack: Attacker's attack - defender's defense.

Skill: (Attacker's attack - defender's defense) * skill's rate.

Bleeding: If some side is bleeding, he/it will lose 10% of max HP every time he/it attacks.

### Controls

Players completely control the game via voice. Feedbacks include Alexa voice, and display, if there is a screen on the device.

## Game Elements

### Roles

Player: Lin, apprentice of the Master. 

Four Holy Beasts: These are the Azure Dragon of the East, the Vermilion Bird of the South, the White Tiger of the West, and the Black Turtle (also called "Black Warrior") of the North.

Yellow Dragon: The master, central guardian.

### Possible Skills

Thump: A high rate attack skill.

Pierce: A higher rate attack skill.

Blade: Bleeding. Lose HP when normal attacking.

Cross Strike: Bleeding. A higher rate than Blade.

Cold Bolt: Frozen. Decrease normal attack speed.

Blizzard: Frozen. A higher rate than Cold Bolt.

### Possible Random Events

Find a sword: This increases Lin's attack.

Fall over: This decreases Lin's attack.

Find a portion: This either gives Lin extra HP or lose some HP.

Find a shield: This increases Lin's defense.

Attacked by a slime: This decreases Lin's defense.

### Possible Bosses

For floors of 1,2,3,5,6,7,9,10,11,13,14,15, the twelve Chinese zodiac signs, rat, ox, tiger, rabbit, dragon, snake, horse, sheep, monkey, rooster, dog and pig, occupy one floor each.

For floors of 4, 8, 12, 16, the Four Holy Beasts, which are the Azure Dragon of the East, the Vermilion Bird of the South, the White Tiger of the West, and the Black Tortoise of the North, guard each floor.

For the last floor, 17, the Yellow Dragon takes the responsibility.

## Development Platform

### Amazon Alexa

Alexa is Amazon's voice recognition service, the brain behind Amazon's Echo, Echo Dot and Echo Show speakers. Alexa provides computing power and recognition *skills* to make it easier for customers to create a more personal experience. Currently, more than 15000 voice skills are available from Starbucks, Uber, Capital One, and other creative designers and developers.

This game project is an Amazon Alexa custom skill. Note that the *skill* here is different from the skill in the previous section.

To complete a custom skill project, it is necessary to have a structure of models, lambda and skill manifest. For more details, see section [6 Components](# Components).

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

Users say a skill's **invocation name** to begin an interaction with a particular custom skill. This skill's invocation name is "Daily Dungeon". Users can say: "Open Daily Dungeon" to launch the skill. 

#### Lambda Function

Lambda function in a custom skill for Alexa is a web service that accepts requests from and sends responses to the Alexa service in the cloud. The web service can be written in any programming language, as long as it meets the requirements below. [^WS]

[^WS]:https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-a-web-service.html

1. The service must be accessible over the Internet.
2. The service must accept HTTP requests on port 443.
3. The service must support HTTP over SSL/TLS, using an Amazon-trusted certificate. Your web service's domain name must be in the `Subject Alternative Names` (SANs) section of the certificate. For testing, you can provide a self-signed certificate.
4. The service must verify that incoming requests come from Alexa. 
5. The service must adhere to the Alexa Skills Kit interface.

The service was developed using Python with the Alexa Skills Kit (ASK) SDKs for Python to verify that requests to the web service do come from Alexa. Also, [AWS Lambda](# AWS Lambda) was used to host my web service, which will be mentioned later.

The AWS Lambda requires that its handler's name is the same as the main code file. If the handler's name is `main.handler`, then it calls the handler methods defined in `main.py`.

In `main.py`, handlers are defined here, each processing a certain intent or a kind of request. For more details, see Chapter [Module Design](# Module Design).

#### Session

The skill can keep the *skill session* open to conduct a back-and-forth interaction with the user. While the session is open, the user does not need to use the invocation name to talk to the skill. [^S]

[^S]: https://developer.amazon.com/docs/custom-skills/manage-skill-session-and-session-attributes.html

Lifecycle of a skill session [^S]:

1. A skill session begins when a user invokes your Alexa skill and Alexa sends your skill a request. The request contains a session object that uses a Boolean value called `new` to indicate that this is a new session.

2. The skill receives the request and returns a response for Alexa to speak to the user.

3. What happens next depends on the value of the `shouldEndSession` parameter in the skill's **response**:

   - `true` – The session ends. Alexa, not the skill, handles any further speech from the user. If the user re-invokes the skill, Alexa creates a new session (that is, go back to step 1).

   - `false` – The session stays open and Alexa opens the microphone to indicate that she expects the user to respond. If the user's response maps to your interaction model, a new intent is sent to the skill and the process goes back to step 2.

     However, if eight seconds elapse without a response from the user, Alexa closes the microphone. If the skill specified a reprompt, Alexa reprompts the user to speak and opens the microphone for eight more seconds. If the user still does not respond, the session is terminated.

     The session may remain open for a few more seconds with the microphone closed if the skill is used on a device with a screen.

   - `undefined` (not set or `null`) – The session's behavior depends on the type of Echo device that the user is interacting with and the content of the response. 

For most of my intents, I set the `shouldEndSession`to `false`, because a game should not end just because the user is thinking for a long time.

#### Cards

Interactions between a user and an Alexa device can include **home cards** displayed in the Amazon Alexa App, the companion app available for Fire OS, Android, iOS, and desktop web browsers. An Alexa-enabled device with a screen also displays cards that have been designed for display in the Alexa app.

![card](../images/card.jpg)

#### Display Templates

A skill developed for Alexa-enabled devices with a screen can also support **display templates**, which are similar to *cards* and are viewed directly on the screen.

![display](../images/display.jpg)

### AWS Lambda

The easiest way to build the cloud-based service for a custom Alexa skill is to use AWS Lambda, an Amazon Web Services offering that runs code only when it's needed and scales automatically, so there is no need to provision or continuously run servers.  [^AL]

The code for my Alexa skill was uploaded to AWS Lambda and it does the rest, executing it in response to Alexa voice interactions and automatically managing the compute resources.

[^AL]: https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html

### Amazon DynamoDB

It is inevitable to have to store attribute information as described in section [Persistent data](# Persistent data). We can store them as session attributes, but they would be lost after the session ends. For those attributes that need to be persistent, we need to use a database to store them. Fortunately, the ASK-SDK for Python allows us to get full access to DynamoDB. 

Amazon DynamoDB is a fully managed proprietary NoSQL database service that supports key-value and document data structures. [^DDB]

[^DDB]:https://en.wikipedia.org/wiki/Amazon_DynamoDB



## Components 

The details of Daily Dungeon Alexa skill components mentioned in section [Amazon Alexa](Amazon Alexa) are as follows.

### Manifest

The following is some key metadata in the manifest, which is described using JSON.

- Publishing Information
  - locales/en-US
    - name: "Daily Dungeon"
    - description: "An role playing game with idle game element in it."
    - summary: "Launch the skill"
    - example phrases: ["open daily dungeon"]
  - category: "GAMES"
- APIs
  - custom
    - endpoint                            #  where the service locates
      - sourceDir: "lambda/py/lambda_upload"
      - uri: "ask-custom-Demo-default"
    - interfaces : [ "RENDER_TEMPLATE"]                          # it is necessary to display

Publishing Information is to determine how the skill is presented to end users in the skill store or Alexa app. APIs specify required information for all interfaces that a skill supports.

### Interaction Model

The following represents some key *intents* and their utterances.

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

### Persistent Data

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

The handler firstly checks whether there are already persistent attributes for a character in the database. If not, it will create a new `Character` and store it in the database. If so, it will load the `Character` and call its `claim_loot` method to claim what the character farms during the offline time. Alexa then will tell users how long they have been offline and how much EXP they obtained.

Also, the attribute `in_maze` tells if Lin is still in a maze or not. Then Alexa will help users remember where they were at the end of last conversation with Alexa.

![launch](../images/launch.jpg)

#### CheckMessagesIntent

During offline time, additional skills may be acquired. Note that our hero, Lin, will level up when he receives enough EXP during the offline farming. Lin acquires a corresponding new skill when he gets to a certain level. Therefore, we need to acknowledge the player what have been acquired. Such messages will be stored as a persistent attribute, which can be read when the player log in.

The handler loads the message attribute as a queue, reads the first one out, and pop it out of the queue. The handler only reads one at a time of this intent.

#### EnterMazeIntent

The `EnterMazeIntent` is the first part of main content of Daily Dungeon. Players need to enter the maze before they canexplore it and finally challenge the boss.

At first, the handler checks `in_maze` to determine if Lin has a uncompleted maze. If so, it will tell the user to resume or discard the maze instead of entering a new one. 

If Lin has not entered any maze on this floor, it will create a `Maze` object. The creation refers to the hard code in `data.py`.  Also, the handler will create a `TempCharacter` object to store temporary status for oncoming random events, because the temporary buffs or debuffs will go when Lin exits or discards a maze. These objects will be stored as persistent attributes. It then tells the user that Lin is in the initial room and encourages them to move.

#### ResumeMazeIntent

If the session ends before Lin successfully defeats the boss, then the user needs to decide either to resume the old session or to discard it. If the user resumes it, the handler will change `in_maze` to IN that indicates the user can give orders like move or fight.

#### DiscardMazeIntent

Similar to `ResumeMazeIntent`, `DiscardMazeIntent` is the other choice when Lin is still in the maze but the user does not want to continue. Generally, it happens when the user has triggered too many bad events to fight the boss. Fortunately, we provide this option to allow the player to start it over. The handler change  `in_maze` to NO that indicates there is no more maze in use.

#### MoveIntent

This intent is triggered when the player is trying to move to another room. What the player said should include a specific direction, north, east, south or west. If not, the handler will tell the player to specify one. 

When the handler retrieves the direction, it loads the `Maze`, the current `Room`, the `Character` and the `TempCharacter`. Based on the current maze and the current room, it can find if there is a room at that direction. If not, it tells the user to pick up another direction. 

If there is a room at that direction, it changes the current `Room` to the new one and sets the new room as *visited*. It then checks the new room's type to see if it has a random event to trigger. If so, it puts the obtained buff or debuff on the `TempCharacter`. The player will be told what has been encountered.

If the new room is the boss room, Lin will be able to fight the boss. The handler sets a boolean persistent attribute `ready_for_boss` to store it.

#### LocationIntent

It is easy for a player to lose their way, especially right after resuming a maze after a long time of offline. This can be attributed to the fact that Alexa is not a visual platform. There is no map for a maze, so players need to have a rough image in their mind about the what the maze looks like. We provide `LocationIntent` to help players remember where they are, where they have been and where they have not.

The handler loads the `Maze` and the current `Room`. It traverses the current room's four directions in random order. Then it tells the user the current room's id and the first direction it found not visited.

#### ChallengeBossIntent

The goal of entering a maze is to find the boss and defeat it. When Lin is in the boss room and able to fight the boss, the player can give their intent to have Lin fight. 

The handler firstly checks `ready_for_boss` to ensure Lin is in the boss room. It creates a `Battle` object to manage the whole battle. The `Battle` requires the `Character` and `TempCharacter` and returns the battle result and its log information. For more information, see section [7.3.2 Battle](#Battle). If Lin wins, the handler sets `in_maze` to NO and puts Lin into the next floor. The handler stores the battle log as a session attribute for the player to review later.

#### BattleLogIntent

Players can review the last battle log for next try to fight the boss. With the information, it is easy to see what happened during the battle and so that players have another try with another skill or just wait for Lin to farm and get stronger.

The handler loads the battle log attribute, if any. It then allows Alexa to read it out. If there is a screen on the device, it will display the details of every move of both sides, Lin and the enemy.

![battle.jpg](https://s2.ax1x.com/2019/07/01/Z3fAje.jpg)

#### ChangeSkillsIntent

It is quite normal when Lin successfully beats the boss of the previous floor but fails on the current floor with the same skill. Therefore, players need to make a choice on which skill to use on a certain boss.

The handler tries to get the slot value of *skill* in users' input. When it obtains the new skill name, the handler sets the new skill for the current equipped skill. Then it stores it in the database.

#### BossInfoIntent

Players may want to better know the boss they are going to fight. We provide this intent to help users adjust their tactics before they start a battle.

The handler tries to look for the boss's name in users' spoken input. If there is not a boss's name in the input, it will by default retrieve Lin's current floor's boss name. The handler then gets the hard code boss information from `data.py` and put it into a sentence, as well as into a Card or a Display Template, if there is a screen in users' device. This kind of data will never change so it is not necessary to store them in a database.

#### SkillsInfoIntent

Similar to `BossInfoIntent`, players may want to know what the skills they know actually do or the exact statistics of a certain skill. `SkillsInfoIntent` is used for this purpose.

The handler retrieves information from `data.py` and then gives it to users with voice and display.

#### CheckStatusIntent

This intent is to tell the player the current statistics of Lin, including attack, defense, hp, mp, level, floor, and the current equipped skill.

The handler loads the information from database and then gives it to users with voice and display.

![stats](../images/stats.jpg)

#### CheckSkillsIntent

This intent is to tell the player what skills has Lin learned. Players can pick up a suitable skill for fighting a certain boss after they know the information.

The handler loads the information form database and then gives it to users with voice and display.

### Other Classes

To make the handlers code clear and organized, several classes and data were implemented, including Character, Mob, Battle, Maze, Data, and their methods for the handlers to use. For more details, see section [7 Module Design](#Module Design).

## Module Design

### Handlers

The intent handlers are in the `hello_world.py` file, which is the lambda function entry. This part has been explained in section [6.4 Intent Handlers](#Intent Handlers).

### Character & Mob

This module includes `Character`, `TempChararacter` and `Mob`.

#### Character

Lin's game statistics, including attack, defense, last offline time, messages and etc., are represented as attributes in `Character` class. It has methods `to_dict` and `from_dict` to put these values to Python dictionary and retrieve them from the dictionary.

The `claim_loot` method calculates how long it has been since the user last logged out. According to the time difference, along with the floor value, it gives Lin a certain number of EXPs. When Lin's EXP value meets the number to level up, Lin levels up and increases his statistics. If a skill should be acquired on this level, the player will be notified.

The `battle_with_boss` method takes a parameter of `TempCharacter`. It retrieves the floor-related boss. It creates a `Battle` object to manage the whole battle between Lin and the boss. When it finished, it returns the result and battle log.

#### TempCharacter

This class stores the temporary statistics obtained in random events. It has similar attributes as a`Character` as well as attack gauge and cast gauge. 

Also, it has `process` method requiring parameters of current room and character. Depending on the room's type, i.e., the random event, it modifies its attributes.

#### Mob

The Mob class is to store information of bosses. It is simple that there are only basic attributes and a `from_dict` method in it.

### Battle Manager

This module includes `Battle` class and `Timer` class.

#### Timer

In this game, due to the battle is calculated in a moment, I use the concept of time to represent the progress of a gauge. Therefore, the timer does not count time, but the progress of gauges. 

At the first of a round, both sides' attack and cast gauges increase by 1 simultaneously, which is called a *tick* of the timer. After the tick, there are judgments whether an attack or a skill should be performed.

A tick also decides whether a debuff, such as Frozen and Bleeding, should end.

#### Battle

The `fight` method is the main method in `Battle` class, which proceeds an entire battle until one side loses all of its HP.

The following is the pseudo code of `fight`.

```pseudocode
WHILE NOT check_death():
	tick()
	
	# Check if player can normal attack
	IF player.attack_gauge>= 100/(player.agility/100)
		player.normal_attack()
	END
	IF check_death()
		BREAK
	END
	
	# Check if play can use skill
	IF player.cast_gauge >= skill['cast']/(self.player.dexterity/100)
		player.move()
	END
	IF check_death()
		BREAK
	END
	
	# Check if the monster can attack or use skill
	...
END
log('Who won and who died.')
RETURN check_death()
```

In `normal_attack`, the attack_gauge is reset to 0 at first. It then calculates the damage using attack and defense, and subtracts the damage value from the enemy's HP. If there is a *Bleeding* status, it subtracts 10% HP from own HP. Then everything happened should be logged.

In `use_skill`, similar to `normal_attack`, the cast_gauge is reset to 0. Then it calculates the damage using attack and defense and the skill's rate, and subtracts the damage value from the enemy's HP. Also, the caster should consume some MP depending on the skill. If the skill has an effect like *Bleeding*, the effect is added to the enemy. Everything that occurs should be logged.

The `check_death` method checks if either side has got its HP to 0. If so, the battle ends.

The `log` method records all the events that happened throughout the battle. It includes some formats of log information, voice, text, card, display.

### Maze

This module includes `Maze` and `Room`.

In `Room`, there are several attributes, *id*, *room ids in four directions*, *room_type* and *is_visited*. These attributes are stored using Python dictionary.

The `Maze` class consists of the current `Room` and a `Room` set. It needs to be initiated with the floor number. It retrieves the constant data from `data.py`.

### Data

In `data.py`, there are some constant data that other modules may use.

`PLAYER_AVATAR`, `MONSTER_AVATAR` and `EMOJI_STATUS` are image URLs. In some intents, these images need to be displayed on the screen.

`EXP_TO_LEVEL_UP` is a list of how many EXP Lin need to level up.

`EXP_PER_ROUND` is a list of how many EXP Lin can obtain per 20 seconds during offline time.

`BOSS_OF_FLOOR` is a list of bosses on each floor.

`MOB_INFO` is a dictionary of statistics of all bosses.

`SKILL_ACQUIRE` is a list of which skill Lin can acquire on each level.

`SKILL_INFO` is a dictionary of statistics of all skills.

`MAZE_OF_FLOOR` is a list of mazes on each floor.



## Conclusions

### Strengths

Daily Dungeon is easy to get used to. Because it is based on Alexa, a voice-interaction platform, the game does not require a sophisticated way to operate it, where voice is enough. It does not have a complex game system for players to get used to.

It helps players exercise a sense of space and improve memory. There is not a visualized map for a maze, even on a device with a screen, players need to have an image of the maze when they are exploring it. If necessary, paper and pencils are recommended.

The game prevents players from playing it for too long, thanks to its offline farming system. Players can have fun exploring mazes and challenging bosses before their characters are too weak to go on. They will realize that their characters need some time to grow. 

The game is an alternative to kill time. When users have some time confetti of 10 to 20 minutes, instead of iPad or phone, they have another choice now, to launch Alexa.

### Limitations

Players may find it not satisfying of Alexa to misunderstand their orders sometimes. This include two kinds of misunderstanding. Firstly, There are multiple ways to express an intent. For example, the move intent has utterances of go north, head north or move to the north. However, there is always another way to express that, which is not included in my intent's utterances. Secondly, Alexa may not get every word exactly for every time, especially there is noise on background.

The difficulty can be too low or too high sometimes. It is very hard to come up with proper numbers for character and boss statistics. I tried to make it as balance as I can. I expect that players launch Daily Dungeon every 4 to 12 hours, so that they may have a good experience that it is neither to hard nor too simple to pass a floor.

The background story is not appealing at all because I am not a good story maker.

## References



