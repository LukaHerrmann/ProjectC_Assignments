import random


class CodeMaster_Computer():
    def makecode(self, allcolors, length):
        '''Deze functie maakt een willekeurige code bestaande uit een aantal elementen die willekeurig gekozen
        zijn uit een gegeven lijst met alle mogelijkheden'''
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
        '''Deze functie zet een tuple van het aantal black en white pins om in een lijst met black en white
        uitgeschreven voor de visuele uitvoering'''
        pins = ['black' for x in range(feedback[0])] + ['white' for y in range(feedback[1])]
        return pins


    def makefrequencydict(self, list):
        '''Deze functie maakt een dictionary met hoevaak bepaalde items voorkomen in een lijst'''
        freq = {}
        for item in list:
            if item in freq.keys():
                freq[item] += 1
            else:
                freq[item] = 1
        return freq


class CodeMaster_Player():
    def colortonumb(self, colors, allcolors):
        '''Deze functie zet een gegeven lijst met kleuren om in een kleuren om het voor dit deel
        van het programma overzichtelijker te maken'''
        result = ''
        for color in colors:
            result += str(allcolors.index(color))
        return result


    def numbtocolor(self, number, allcolors):
        '''Deze functie zet de meegegeven cijfers om in de bij behorende kleuren die gebruikt
        kunnen worden in de interface van het spel'''
        return [allcolors[int(x)] for x in number]


    def getpossiblecombinations(self, allnumbers):
        '''Deze functie maakt een lijst met alle mogelijke combinaties van 4 elementen met een aangegeven
        hoeveelheid mogelijkheden'''
        possibilites = []
        for number1 in allnumbers:
            for number2 in allnumbers:
                for number3 in allnumbers:
                    for number4 in allnumbers:
                        possibilites.append(f'{number1}{number2}{number3}{number4}')
        return possibilites


    def newposibilities(self, possibilities, guess, feedback):
        '''Deze functie gaat door het aantal gegeven mogelijkheden en checkt voor elke mogelijkheid
        of deze een mogelijke oplossing kan zijn voor een gegeven code de feedback te berekenen bij
        alle mogelijkheden'''
        new = []
        for possibility in possibilities:
            #hierbij wordt gebruik gemaakt van een functie uit de module waarbij de computer de codemaster
            #is om te bepalen wat de black en white pins zijn bij de codes
            tempfeedback = CodeMaster_Computer.determinepins(CodeMaster_Computer, guess, possibility)
            if tempfeedback == feedback:
                new.append(possibility)
        return new


    def getfeedback(self, list):
        '''Deze functie haalt de feedback op die de speler als codemaster heeft ingevoerd en zet deze om
        in een black, white tuple'''
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


    def worstcase(self, code, cases, possibilities):
        '''Deze functie bepaalt voor elke case hoeveel mogelijkheden er nog overblijven van het totaal aantal
        mogelijkheden. De functie returnt dan het grootste aantal wat van het totaal aantal mogelijkheden
        kan overblijven'''
        worst = max([len(CodeMaster_Player.newposibilities(CodeMaster_Player, possibilities,
                                                           code, case)) for case in cases])
        return worst