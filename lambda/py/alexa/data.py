EXP_TO_LEVEL_UP = [
    300,  # 1
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
    'Awakened Shrub',
    'Awakened Shrub two'
]

MOB_INFO = {
    'Monster A': {
        'attack': 20,
        'defense': 0,
        'hp': 100,
        'mp': 0,
        'skills': [],
        'speed': 100,
        'cast_speed': 100
    },
    'Awakened Shrub': {
        'attack': 20,
        'defense': 0,
        'hp': 200,
        'mp': 0,
        'skills': [],
        'speed': 100,
        'cast_speed': 100
    },
    'Awakened Shrub two': {
        'attack': 2000,
        'defense': 0,
        'hp': 3000,
        'mp': 0,
        'skills': ['Double Strafe'],
        'speed': 100,
        'cast_speed': 100
    }
}

SKILL_INFO = {
    'Double Strafe': {
        'name': 'Double Strafe',
        'rate': 380,
        'cast': 300,
        'mp': 20
    }
}
