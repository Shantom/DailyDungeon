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
    'awakened shrub',
    'minotaur',
    'skeleton',
    'skeleton',
    'skeleton',  # 5
    'skeleton',
    'skeleton',
    'skeleton',
    'skeleton',
    'skeleton',  # 10
    'skeleton',
    'skeleton',
    'skeleton',
    'skeleton',
    'skeleton',  # 15
    'skeleton',
]

MOB_INFO = {
    'awakened shrub': {
        'attack': 20,
        'defense': 0,
        'hp': 2000,
        'mp': 0,
        'skill': None,
        'speed': 100,
        'cast_speed': 100
    },
    'minotaur': {
        'attack': 50,
        'defense': 0,
        'hp': 400,
        'mp': 100,
        'skill': 'Thump',
        'speed': 100,
        'cast_speed': 50
    },
    'skeleton': {
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
    'Blade',
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
