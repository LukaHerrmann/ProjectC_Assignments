import random


def colortonumb(colors, allcolors):
    result = ''
    for color in colors:
        result += str(allcolors.index(color))
    return result


def numbtocolor(number, allcolors):
    return [allcolors[int(x)] for x in number]


def getpossiblecombinations(allnumbers):
    possibilites = []
    for number1 in allnumbers:
        for number2 in allnumbers:
            for number3 in allnumbers:
                for number4 in allnumbers:
                    possibilites.append(f'{number1}{number2}{number3}{number4}')
    return possibilites


def makepinfeedback(pins):
    black = 0
    white = 0
    for pin in pins:
        black += (pin == 'black')
        white += (pin == 'white')
    return black,white


def generate_feedback(code, guess):
    pass


def newposibilities(posibilities, guess, feedback):
    pass
