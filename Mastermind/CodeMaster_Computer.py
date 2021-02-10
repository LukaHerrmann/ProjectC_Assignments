import random


def makecode(allcolors, length):
    code = [random.choice(allcolors) for x in range(length)]
    return code


def determinepins(code, guesscolors):
    '''Eerst maakt de functie dictionaries van de twee kleurencombinaties. Om het aantal zwarte pinnen te berkenen
    worden de items in de verschillende invoerwaardes met elkaar vergeleken. Om het aantal witte pinnen te berekenen
    wordt het minimale aantal genomen van de frequency waardes van de code en de kleurinvoer en vervolgens wordt
    het aantal zwarte pinnen ervan afgetrokken, omdat daarmee niet rekening wordt gehouden.'''
    # methode om witte pins te berekenen van TigerhawkT3 op YouTube
    # link: https://www.youtube.com/watch?v=Hv47MO1vQAo
    codefreq = makefrequencydict(code)
    guessfreq = makefrequencydict(guesscolors)
    black = sum([x == y for x, y in zip(code, guesscolors)])
    white = sum(min(codefreq[x], guessfreq[x] if x in guessfreq.keys() else 0) for x in codefreq.keys())
    white -= black
    pins = ['black' for x in range(black)] + ['white' for y in range(white)]
    return pins


def makefrequencydict(list):
    freq = {}
    for item in list:
        if item in freq.keys():
            freq[item] += 1
        else:
            freq[item] = 1
    return freq