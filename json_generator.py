import json

rooms = {
    'inner dungeon': {
        'directions': {'south': 'outer dungeon'},
        'description': [
            "The bars of your cage are ridiculously far apart,",
            "it won't be a problem to squeeze out.",
            "There is also a door on the SOUTH wall."
        ],
        'items': [],
        'map':  (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |  X  |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    )

    },

    'outer dungeon': {
        'directions': {'north': 'inner dungeon', 'west': 'main hallway'},
        'description': [
            "There is a skeleton. It has energy drink in  it's hands.",
            "If only you would have GLOVES to TAKE THE DRINK",
            "You can go WEST and NORTH from here."
        ],
        'items': ['energy drink'],
        'map': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________   X  |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    )
    },

    'main hallway': {
        'directions': {'south': 'the great hall', 'west': 'entrance', 'north': 'laboratory', 'east': 'outer dungeon'},
        'description': [
            "Nothing to watch here except macabre paintings.",
            "You do not have time for this.",
            "You can go all directions from here."
        ],
        'items': [],
        'map':  (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __         X         ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    )
    },

    'the great hall': {
        'directions': {'north': 'main hallway', 'east': 'bed chambers'},
        'description': [
            "That's likely where the 'party' is suppose to be held.",
            "The hall is huge and not well maintained.",
            "Dust, spiderweb, and blood stains are everywhere.",
            "You see a pizza box in the corner.",
            "You are hungry, so take a TAKE A SLICE.",
            "You can go EAST and NORTH from here."
        ],
        'items': ['slice of pizza'],
        'map': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |        X          _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    )
    },

    'laboratory': {
        'directions': {'south': 'main hallway', 'east': 'library'},
        'description': [
            "That is where the undead do their unholy research.",
            "Walls are covered with jars,",
            "containing some wierd creatures.",
            "Some of them are staring at you.",
            "THE GLOVES!",
            "You can only go EAST and SOUTH."
        ],
        'items': ['gloves'],
        'map':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                (o__0)   (@__@)  (X__x)                                                                                                _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |        X         _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
      )
    },

    'bed chambers': {
        'directions': {'west': 'the great hall'},
        'description': [
            "The room is pretty much empty,",
            "except for the fancy coffin in the very center.",
            "The lid is closed for now.",
            "After closer inspection,",
            "you see a KEY laying nearby the coffin.",
            "You can only go WEST from here."
        ],
        'items': ['key'],
        'map':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _   X   |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
     )
    },

    'library': {
        'directions': {'west': 'laboratory'},
        'description': [
            "Endless rows of books.",
            "You are only interested in that KARATE GUIDE.",
            "You can only go WEST from here."
        ],
        'items': ['karate guide'],
        'map': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _   X   |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),
    },

    'entrance': {
        'directions': {},
        'description': [
            "Escape is here!",
            "The doors shut behind you."
            "The henchman is guarding the exit,",
            "and you are not ready to take on him.",
            "He grins at you, and you go back slowly.",
            "The doors are supper heavy",
            "It takes you quite a few seconds to open them.",
            "You lost precious time.",
            "YES, THERE IS A TIME PENALTY FOR THIS ROOM!"
        ],
        'items': [],
        'map':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\     X   __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ) 
    },
}

with open('rooms.json', 'x+') as f:
    content = json.dumps(rooms)
    f.writelines(content)
