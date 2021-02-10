import random


class CodeMaster_Computer():
    def makecode(self, allcolors, length):
        code = [random.choice(allcolors) for x in range(length)]
        return code


    def determinepins(self, code, guesscolors):
        '''Eerst maakt de functie dictionaries van de twee kleurencombinaties. Om het aantal zwarte pinnen te berkenen
        worden de items in de verschillende invoerwaardes met elkaar vergeleken. Om het aantal witte pinnen te berekenen
        wordt het minimale aantal genomen van de frequency waardes van de code en de kleurinvoer en vervolgens wordt
        het aantal zwarte pinnen ervan afgetrokken, omdat daarmee niet rekening wordt gehouden.'''
        # methode om witte pins te berekenen van TigerhawkT3 op YouTube
        # link: https://www.youtube.com/watch?v=Hv47MO1vQAo
        codefreq = self.makefrequencydict(code)
        guessfreq = self.makefrequencydict(guesscolors)
        black = sum([x == y for x, y in zip(code, guesscolors)])
        white = sum(min(codefreq[x], guessfreq[x] if x in guessfreq.keys() else 0) for x in codefreq.keys())
        white -= black
        pins = ['black' for x in range(black)] + ['white' for y in range(white)]
        return pins


    def makefrequencydict(self, list):
        freq = {}
        for item in list:
            if item in freq.keys():
                freq[item] += 1
            else:
                freq[item] = 1
        return freq


class CodeMaster_Player():
    def colortonumb(self, colors, allcolors):
        result = ''
        for color in colors:
            result += str(allcolors.index(color))
        return result


    def numbtocolor(self, number, allcolors):
        return [allcolors[int(x)] for x in number]


    def getpossiblecombinations(self, allnumbers):
        possibilites = []
        for number1 in allnumbers:
            for number2 in allnumbers:
                for number3 in allnumbers:
                    for number4 in allnumbers:
                        possibilites.append(f'{number1}{number2}{number3}{number4}')
        return possibilites


    def makepinfeedback(self, pins):
        black = 0
        white = 0
        for pin in pins:
            black += (pin == 'black')
            white += (pin == 'white')
        return black, white


    def generate_feedback(self, code, guess):
        pass


    def newposibilities(self, posibilities, guess, feedback):
        pass
