
def show_hagman(lives):
    available_lives = {
        0: show_dead(),
        1: show_1_left(),
        2: show_2_left(),
        3: show_3_left(),
        4: show_4_left(),
        5: show_5_left(),
    }

    print('\n'.join(available_lives.get(lives)))


def show_dead():
    return ['   ------',
            '   |    O',
            '   |  /| |\ ',
            '   |    ||',
            '   |    ""',
            '  /|\ ',
            '  ---------']


def show_1_left():
    return ['   ------',
            '   |    O',
            '   |  /| |\ ',
            '   |    |',
            '   |    "',
            '  /|\ ',
            '  ---------']

def show_2_left():
    return ['   ------',
            '   |    O',
            '   |  /| |\ ',
            '   |    ',
            '   |    ',
            '  /|\ ',
            '  ---------']


def show_3_left():
    return ['   ------',
            '   |    O',
            '   |  /| |',
            '   |    ',
            '   |    ',
            '  /|\ ',
            '  ---------']

def show_4_left():
    return ['   ------',
            '   |    O',
            '   |',
            '   |',
            '   |',
            '  /|\ ',
            '  ---------']

def show_5_left():
    return ['   ------',
            '   |',
            '   |',
            '   |',
            '   |',
            '  /|\ ',
            '  ---------']
