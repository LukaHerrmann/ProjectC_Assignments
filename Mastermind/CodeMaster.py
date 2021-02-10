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
        codefreq = self.makefrequencydict(self, code)
        guessfreq = self.makefrequencydict(self, guesscolors)
        black = sum([x == y for x, y in zip(code, guesscolors)])
        white = sum(min(codefreq[x], guessfreq[x] if x in guessfreq.keys() else 0) for x in codefreq.keys())
        white -= black
        return black, white


    def feedbacktocolor(self, feedback):
        pins = ['black' for x in range(feedback[0])] + ['white' for y in range(feedback[1])]
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


    def newposibilities(self, possibilities, guess, feedback):
        new = []
        for possibility in possibilities:
            tempfeedback = CodeMaster_Computer.determinepins(CodeMaster_Computer, guess, possibility)
            if tempfeedback == feedback:
                new.append(possibility)
        return new


    def getfeedback(self, list):
        feedbackdict = CodeMaster_Computer.makefrequencydict(CodeMaster_Computer, list)
        if 'black' in feedbackdict.keys():
            black = feedbackdict['black']
        else:
            black = 0
        if 'white' in feedbackdict.keys():
            white = feedbackdict['white']
        else:
            white = 0
        return black, white