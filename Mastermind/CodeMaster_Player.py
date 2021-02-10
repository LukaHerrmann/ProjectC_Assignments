import random


def colortonumb(colors, allcolors):
    result = ''
    for color in colors:
        result += str(allcolors.index(color))
    return result


def numbtocolor(number, allcolors):
    return [allcolors[int(x)] for x in number]