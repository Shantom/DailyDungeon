PLAYER_AVATAR = 'https://s2.ax1x.com/2019/07/01/Z3fCh6.jpg'
PLAYER_STANDING = 'https://s2.ax1x.com/2019/07/01/Z36YHP.png'
MONSTER_AVATAR = {
    '?': 'https://www.pixilart.com/images/art/5c9c4148ae83dd8.png',
    'boarbow': 'https://www.pixilart.com/images/art/7a500637e457561.png',
    'ratpier': 'https://www.pixilart.com/images/art/3502890adb853ee.png',
    'broadbull': 'https://www.pixilart.com/images/art/c04bf692bb7c44b.png',
    'black tortoise': 'https://www.pixilart.com/images/art/81970b006afbac3.png'
}


EMOJI_STATUS = {
    'Bleeding': "<img src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/drop-of-blood_1fa78.png' width='20' height='20' />",
    'Frozen': "<img src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/freezing-face_1f976.png' width='20' height='20' />"
}

EXP_TO_LEVEL_UP = [
    30,  # 1
    1000,
    2700,
    5000,
    8000,  # 5
    15000,
    30000,
    40000,
    50000,
    61000,  # 10
    80000,
    103000,
    134000,
    156000,
    180000,  # 15
    999999999999
]

COIN_PER_ROUND = 50

EXP_PER_ROUND = [
    33,  # 1
    35,
    38,
    40,
    50,  # 5
    55,
    60,
    65,
    70,
    80,  # 10
    87,
    92,
    97,
    105,
    120,  # 15
    128
]

BOSS_OF_FLOOR = [
    'boarbow',
    'ratpier',
    'broadbull',
    'black tortoise',

    'tigermortar',
    'bunnyblast',
    'drident',
    'azure dragon',

    'whiptail',
    'thoroughblade',
    'ramram',
    'vermilion bird',

    'hammerkong',
    'kataroost',
    'chakanine',
    'white tiger',

    'yellow dragon'
]

MOB_INFO = {
    'boarbow': {
        'attack': 20,
        'defense': 0,
        'hp': 2000,
        'mp': 0,
        'skill': 'Thump',
        'speed': 100,
        'cast_speed': 100
    },
    'ratpier': {
        'attack': 50,
        'defense': 0,
        'hp': 400,
        'mp': 100,
        'skill': 'Thump',
        'speed': 100,
        'cast_speed': 50
    },
    'broadbull': {
        'attack': 200,
        'defense': 0,
        'hp': 3000,
        'mp': 0,
        'skill': 'Double Strafe',
        'speed': 100,
        'cast_speed': 100
    },
    'black tortoise': {
        'attack': 200,
        'defense': 0,
        'hp': 3000,
        'mp': 0,
        'skill': 'Double Strafe',
        'speed': 100,
        'cast_speed': 100
    },

}

SKILL_ACQUIRE = [
    None,
    'Thump',
    None,
    'Pierce',
    None,
    'Blade',
    None,
    'Cold Bolt',
    None,
    'Cross Strike',
    None,
    'Blizzard',
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

SKILL_INFO = {
    'Double Strafe': {
        'name': 'Double Strafe',
        'rate': 380,
        'cast': 280,
        'mp': 20,
        'effect': None
    },
    'Blitz Beat': {
        'name': 'Blitz Beat',
        'rate': 190,
        'cast': 150,
        'mp': 10,
        'effect': None
    },
    'Arrow Shower': {
        'name': 'Arrow Shower',
        'rate': 710,
        'cast': 500,
        'mp': 40,
        'effect': None
    },
    'Thump': {
        'name': 'Thump',
        'rate': 190,
        'cast': 150,
        'mp': 30,
        'effect': None
    },
    'Blade': {
        'name': 'Blade',
        'rate': 150,
        'cast': 500,
        'mp': 30,
        'effect': 'Bleeding'
    },
    'Blizzard': {
        'name': 'Blizzard',
        'rate': 180,
        'cast': 400,
        'mp': 40,
        'effect': 'Frozen'
    }
}

MAZE_OF_FLOOR = [
    None,
    {  # 1
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': '2',
            'south': '0',
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': '3',
            'south': 'boss',
            'west': '1',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': None,
            'west': '2',
            'room_type': None
        },
        'boss': {
            'id': 'boss',
            'north': '2',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 2
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': '2',
            'south': '0',
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': '3',
            'south': 'boss',
            'west': '1',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': None,
            'west': '2',
            'room_type': 'ATTUP'
        },
        'boss': {
            'id': 'boss',
            'north': '2',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 3
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': '2',
            'south': '0',
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': '3',
            'south': '4',
            'west': '1',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': 'boss',
            'west': '2',
            'room_type': 'ATTDOWN'
        },
        '4': {
            'id': '4',
            'north': '2',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'ATTUP'
        },
        'boss': {
            'id': 'boss',
            'north': '3',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 4
        '0': {
            'id': '0',
            'north': '1',
            'east': '3',
            'south': None,
            'west': '2',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': None,
            'south': '0',
            'west': '2',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': '5',
            'east': '1',
            'south': '0',
            'west': None,
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': '6',
            'east': None,
            'south': '0',
            'west': None,
            'room_type': 'ATTUP'
        },
        '4': {
            'id': '4',
            'north': 'boss',
            'east': '6',
            'south': None,
            'west': '5',
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': '4',
            'south': '2',
            'west': None,
            'room_type': 'HEAL'
        },
        '6': {
            'id': '6',
            'north': None,
            'east': None,
            'south': '3',
            'west': '4',
            'room_type': 'POISON'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 5
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '6',
            'east': '3',
            'south': '0',
            'west': '2',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': 'boss',
            'east': '1',
            'south': None,
            'west': None,
            'room_type': 'HEAL'
        },
        '3': {
            'id': '3',
            'north': '5',
            'east': None,
            'south': '4',
            'west': '1',
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': '3',
            'east': None,
            'south': None,
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': None,
            'south': '3',
            'west': None,
            'room_type': 'DEFUP'
        },
        '6': {
            'id': '6',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': None
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '2',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 6
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': 'boss',
            'east': '5',
            'south': None,
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': 'boss',
            'south': None,
            'west': None,
            'room_type': 'HEAL'
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': 'boss',
            'west': None,
            'room_type': 'ATTUP'
        },
        '4': {
            'id': '4',
            'north': None,
            'east': None,
            'south': None,
            'west': 'boss',
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': None,
            'south': '6',
            'west': '1',
            'room_type': None
        },
        '6': {
            'id': '6',
            'north': '5',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'ATTUP'
        },
        'boss': {
            'id': 'boss',
            'north': '3',
            'east': '4',
            'south': '1',
            'west': '2',
            'room_type': 'BOSS'
        }
    },
    {  # 7
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '2',
            'east': '0',
            'south': None,
            'west': 'boss',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': 'POISON'
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': 'boss',
            'west': None,
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': 'boss',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'ATTDOWN'
        },
        '5': {
            'id': '5',
            'north': '6',
            'east': 'boss',
            'south': None,
            'west': None,
            'room_type': None
        },
        '6': {
            'id': '6',
            'north': None,
            'east': None,
            'south': '5',
            'west': None,
            'room_type': 'DEFUP'
        },
        'boss': {
            'id': 'boss',
            'north': '3',
            'east': '1',
            'south': '4',
            'west': '5',
            'room_type': 'BOSS'
        }
    },
    {  # 8
        '0': {
            'id': '0',
            'north': None,
            'east': '2',
            'south': '1',
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '0',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'ATTUP'
        },
        '2': {
            'id': '2',
            'north': '3',
            'east': '5',
            'south': '4',
            'west': '0',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': None,
            'east': None,
            'south': '2',
            'west': None,
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': '2',
            'east': None,
            'south': None,
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': 'boss',
            'south': None,
            'west': '2',
            'room_type': 'HEAL'
        },
        '6': {
            'id': '6',
            'north': None,
            'east': None,
            'south': 'boss',
            'west': None,
            'room_type': None
        },
        'boss': {
            'id': 'boss',
            'north': '6',
            'east': None,
            'south': None,
            'west': '5',
            'room_type': 'BOSS'
        }
    },
    {  # 9
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': '0',
            'south': None,
            'west': '2',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': '3',
            'east': '1',
            'south': None,
            'west': None,
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': None,
            'east': '4',
            'south': '2',
            'west': None,
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': 'boss',
            'east': '5',
            'south': None,
            'west': '3',
            'room_type': 'ATTUP'
        },
        '5': {
            'id': '5',
            'north': None,
            'east': None,
            'south': None,
            'west': '4',
            'room_type': 'HEAL'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 10
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': None,
            'east': '0',
            'south': None,
            'west': '2',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': '1',
            'south': '3',
            'west': 'boss',
            'room_type': 'HEAL'
        },
        '3': {
            'id': '3',
            'north': '2',
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'ATTUP'
        },
        '4': {
            'id': '4',
            'north': '3',
            'east': None,
            'south': None,
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': None,
            'south': 'boss',
            'west': None,
            'room_type': None
        },
        '6': {
            'id': '6',
            'north': 'boss',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'POISON'
        },
        'boss': {
            'id': 'boss',
            'north': '5',
            'east': '2',
            'south': '6',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 11
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '0',
            'east': None,
            'south': '2',
            'west': '3',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': '1',
            'east': None,
            'south': None,
            'west': '4',
            'room_type': 'DEFUP'
        },
        '3': {
            'id': '3',
            'north': None,
            'east': '1',
            'south': '4',
            'west': 'boss',
            'room_type': 'DEFUP'
        },
        '4': {
            'id': '4',
            'north': '3',
            'east': '2',
            'south': None,
            'west': None,
            'room_type': None
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': '3',
            'south': None,
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 12
        '0': {
            'id': '0',
            'north': '3',
            'east': '2',
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '0',
            'east': '2',
            'south': None,
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': '0',
            'east': None,
            'south': None,
            'west': '1',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': 'boss',
            'east': '5',
            'south': '0',
            'west': '4',
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': None,
            'east': '3',
            'south': None,
            'west': '6',
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': '7',
            'south': None,
            'west': '3',
            'room_type': None
        },
        '6': {
            'id': '6',
            'north': None,
            'east': '4',
            'south': None,
            'west': None,
            'room_type': 'ATTUP'
        },
        '7': {
            'id': '7',
            'north': None,
            'east': None,
            'south': None,
            'west': '5',
            'room_type': 'DEFUP'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '3',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 13
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '0',
            'east': None,
            'south': None,
            'west': '2',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': '3',
            'east': '1',
            'south': None,
            'west': None,
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': '4',
            'east': None,
            'south': '2',
            'west': '5',
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': None,
            'east': None,
            'south': '3',
            'west': 'boss',
            'room_type': 'ATTUP'
        },
        '5': {
            'id': '5',
            'north': 'boss',
            'east': '3',
            'south': None,
            'west': None,
            'room_type': 'ATTDOWN'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': '4',
            'south': '5',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 14
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '0',
            'east': '2',
            'south': '5',
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': '3',
            'south': '6',
            'west': '1',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': 'boss',
            'east': None,
            'south': '4',
            'west': '2',
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': '3',
            'east': None,
            'south': None,
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': '1',
            'east': '6',
            'south': None,
            'west': None,
            'room_type': 'DEFDOWN'
        },
        '6': {
            'id': '6',
            'north': '2',
            'east': None,
            'south': None,
            'west': '5',
            'room_type': 'POISON'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '3',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 15
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '2',
            'east': '0',
            'south': '3',
            'west': '4',
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': None,
            'east': None,
            'south': '1',
            'west': None,
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'POISON'
        },
        '4': {
            'id': '4',
            'north': 'boss',
            'east': '1',
            'south': '5',
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': '4',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'ATTUP'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'BOSS'
        }
    },
    {  # 16
        '0': {
            'id': '0',
            'north': None,
            'east': None,
            'south': None,
            'west': '1',
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '2',
            'east': '0',
            'south': None,
            'west': None,
            'room_type': None
        },
        '2': {
            'id': '2',
            'north': 'boss',
            'east': '4',
            'south': '1',
            'west': '3',
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': '5',
            'east': 'boss',
            'south': '2',
            'west': None,
            'room_type': None
        },
        '4': {
            'id': '4',
            'north': '6',
            'east': None,
            'south': '2',
            'west': 'boss',
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': None,
            'east': None,
            'south': '3',
            'west': None,
            'room_type': 'ATTUP'
        },
        '6': {
            'id': '6',
            'north': None,
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'DEFUP'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': '4',
            'south': '2',
            'west': '3',
            'room_type': 'BOSS'
        }
    },
    {  # 17
        '0': {
            'id': '0',
            'north': '1',
            'east': None,
            'south': None,
            'west': None,
            'room_type': 'VISITED'
        },
        '1': {
            'id': '1',
            'north': '2',
            'east': None,
            'south': '0',
            'west': None,
            'room_type': 'ATTUP'
        },
        '2': {
            'id': '2',
            'north': '3',
            'east': None,
            'south': '1',
            'west': None,
            'room_type': None
        },
        '3': {
            'id': '3',
            'north': '4',
            'east': None,
            'south': '2',
            'west': None,
            'room_type': 'DEFUP'
        },
        '4': {
            'id': '4',
            'north': '5',
            'east': None,
            'south': '3',
            'west': None,
            'room_type': None
        },
        '5': {
            'id': '5',
            'north': 'boss',
            'east': None,
            'south': '4',
            'west': None,
            'room_type': 'HEAL'
        },
        'boss': {
            'id': 'boss',
            'north': None,
            'east': None,
            'south': '5',
            'west': None,
            'room_type': 'BOSS'
        }
    }
]
