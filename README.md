# The Daily Dungeon Game via Amazon Alexa

## 1. Overview

### 1.1 Game Name and Running Environment.

Name: Daily Dungeon

Environment: Amazon Alexa

### 1.2 Game Background and Story

#### Background

They are the [Azure Dragon](https://en.wikipedia.org/wiki/Azure_Dragon) of the East, the [Vermilion Bird](https://en.wikipedia.org/wiki/Vermilion_Bird) of the South, the [White Tiger](https://en.wikipedia.org/wiki/White_Tiger_(China)) of the West, and the [Black Turtle](https://en.wikipedia.org/wiki/Black_Tortoise) (also called "Black Warrior") of the North

主角小林跟随师父进入了地下城探寻秘密，不料刚进入地下城的入口，师父就神秘消失了。此时的小林发现地下城的入口被关闭，墙壁上浮现出一行字：须打败四圣兽，方可通过试炼，逃出生天。地下城分为16层，每层有一个守关boss看守，每4层有一个圣兽看守。小林不断地通过击杀当前楼层的小怪获得经验值和金币，提升自己的能力。当小林终于击败四圣兽来到了最终关卡，却发现。。。

Our hero Lin follows master into the dungeon to explore the secret, but as soon as he enters the dungeon entrance, his master mysteriously disappears. 
At this time, Lin found that the gate of the dungeon had been closed, and a line appeared on the wall: defeat the four holy beasts before you could escape from here. 
The dungeon is divided into 16 floors, each guarded by a boss, and every four floors guarded by a holy beast. Lin needs to find a way through a maze before he could fight the boss.
Everyday, Lin beats monsters on the current floor to gain experience and gold coins, with which he gets stronger. 
When Lin finally defeated the four beasts and entered the final floor, only to find that...

### 1.3 Game Features

Daily Dungeon is a role-playing game. Players can help our hero Lin when he needs to make a decision.

每日地牢为角色扮演游戏。玩家可以帮助小林合理选择技能，通过迷宫，击败守关boss。当玩家不在操作时，即未登录游戏时，小林将会自动在当前楼层不断击败小怪来获取经验值和金币。当经验值满足了小林当前等级所需的经验时，小林将会自动升级，并提升各项属性。金币可用来（暂无用处）。当升至特定等级时，小林将领悟特定招式，玩家可帮助小林装备某种招式来应对不同的boss。玩家可指引小林通过迷宫，在迷宫中，小林可能会遇到许多不同的随机事件，这些事件或增加或降低小林的临时属性。

## 2. Game Mechanism

### 2.1 Rules

1. 当玩家不在线时，小林将自动在当前楼层不断击败小怪来获取经验值和金币。

### 2.2 战斗方式

本游戏战斗采用全自动战斗，玩家在战斗之前可通过探索迷宫获取不同的buff，调整携带的技能。对战双方各自拥有两个进度条，一个普通攻击进度条（最高100），一个释放技能进度条（最高1000），每经过一个单位时间，四个进度条各自增加1点，当进度达到所要释放攻击或技能所需要的值后，玩家/怪物将会进行一次攻击/技能，并在攻击过后将进度条减去相应的值。

### 2.3 属性说明（敌我相同）

attack: 增加攻击力可增加对敌人杀伤力的伤害值。一般是衡量人物强与弱的重要指标。

defense:一项决定每次被击中时可以抵消多少伤害的属性

HP(Hit Point): the amount of health 

MP(Magic Point): 使用技能所需要消耗的point

agility（in percentage) :普通攻击速度， 普通攻击需要消耗取整（100/agility) 行动值

dexterity（in percentage)  : 技能释放速度，技能需要消耗取整（技能cast/dexterity）行动值

### 2.4 迷宫房间

每个房间有通往下一个房间的通路，可能存在于四个方向（东南西北）的一个或几个。如果该房间有随机事件，则在进入的时候强制触发。只有在boss房里，才可以挑战boss，一旦挑战成功则自动下一层，且自动退出迷宫。如果挑战失败，则没有惩罚。



### 2.5 玩法

完全语音操作，反馈包括alexa语音和card屏幕显示。

## 3. Game Elements

### 3.1 Roles

Player: Lin, Male, apprentice of the Master. 该游戏为角色扮演类游戏，玩家只可以操纵小林在地下城世界中进行游玩。

四圣兽：四方守护神，镇守五行元素（金木水火）

黄龙：The master，中央守护神，镇守元素（土）

### 3.2 可能出现的技能

重击

疯狂连斩 流血，每次普攻掉血

施毒 中毒，每次技能掉血

断筋 100，停止读条

冰冻 120，减缓普通攻击

治疗 



威吓

### 3.3 可能出现的随机事件

攻击力上升/下降

防御力上升/下降

血量恢复/减少



### 3.4 可能出现的boss

四圣兽：青龙白虎朱雀玄武



## 4. 持久化数据

attribute

- character
  - level
  - floor
  - exp
  - coin
  - attack
  - defense
  - hp
  - mp
  - agility
  - dexterity
  - cur_skill
  - skills
  - sec_per_round
- in_maze
- maze
  - cur_room
    - id
    - east
    - south
    - west
    - north
    - is_visited
    - room_type
  - rooms (dict where key is id and value is like cur_room)
    - ...
- ready_for_boss
- temp_buff

## 5. 模块设计

### 5.1 Character

### 5.2 Mob

### 5.3 Battle

### 5.4 Maze

### 5.5 Data

### 5.6 Intents

#### 5.6.1 Launch request

#### 2 enter maze

#### 3 resume maze

#### 4. discard maze

#### location 

#### move

#### challenge_boss

#### battle_log

#### boss info

#### check status

#### check skill

#### TODO: set skill

## 6. 数值设计

技能

属性

单位时间收益

boss属性

随机事件

## 7. 游戏基本流程





