from tkinter import *



class startscreen():
    '''Deze class betreft het opstartscherm waarbij de speler de keuze krijgt of hij/zij de code wil bedenken
    of raden'''
    playerchoice = None
    def createscreen(self, windowwidth, windowheight, windowtitle, title, bgcolor):
        '''Maakt een scherm aan en geeft die terug'''
        root = Tk()
        # De breedte en hoogte van het scherm ophalen
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        # De voorafgaande informatie gebruiken om de interface in het midden van het scherm te plaatsen
        x_coordinate = int((screenwidth/2) - (windowwidth/2))
        y_coordinate = int((screenheight/2) - (windowheight/2))
        root.geometry('{}x{}+{}+{}'.format(windowwidth, windowheight, x_coordinate, y_coordinate))
        root.configure(bg=bgcolor)
        root.title(windowtitle)
        root.resizable(False, False)
        screentitle = Label(root,
                            text=title,
                            font=('',15,'bold'),
                            bg=bgcolor)
        screentitle.place(relx=0.5, rely=0.15, anchor=CENTER)
        return root


    def createbuttons(self, root, buttoncolor, width, height, spacing):
        '''Maakt de knoppen, zodat de gebruiker de keuze kan maken om de codemaster te zijn
        of de code te raden'''
        codemastercomputer = Button(root,
                                    text='Guess the code',
                                    bg=buttoncolor,
                                    width=width,
                                    height=height)
        codemastercomputer.place(relx=0.5, rely=0.5-spacing, anchor=CENTER)
        codemasterplayer = Button(root,
                                  text='Make the code',
                                  bg=buttoncolor,
                                  width=width,
                                  height=height)
        codemasterplayer.place(relx=0.5, rely=0.5+spacing, anchor=CENTER)
        return codemastercomputer, codemasterplayer


    def gotoCMComputer(self, root):
        '''Deze functie haalt het scherm weg en slaat de keuze 'Guess the code' op in een variabele'''
        #playerchoice is False als de gebruiker wil dat de computer de codemaster is
        startscreen.playerchoice = False
        root.destroy()


    def gotoCMPlayer(self, root):
        '''Deze functie haalt het scherm weg en slaat de keuze 'Make the code' op in een variabele'''
        #playerchoice is True als de gebruiker de codemaster wil zijn
        startscreen.playerchoice = True
        root.destroy()


class CodeMaster():
    '''Deze class verzorgt alle grafische weergaves die nodig zijn om het spel Mastermin weer te geven'''
    #algemene class variabelen om voorbij de functies te tracken
    code = []
    pins = []
    step = 1
    def creategameframe(self, root, width, side, bgcolor):
        '''Deze functie maakt een frame waarin de game gespeeld kan worden en returnt die'''
        mastergame = Frame(root,
                           width=width,
                           bg=bgcolor)
        mastergame.pack(side=side, fill=Y, expand=True, anchor='w')
        return mastergame


    def placecolor(self, frame, color, bordercolor, bgcolor, x, y, width, height):
        '''Deze functie maakt een rondje op basis van de bijgevoegde variabelen en returnt dan het
        canvas object voor het gemaakte rondje'''
        tempcanvas = Canvas(frame,
                            bg=bgcolor,
                            width=width,
                            height=height,
                            highlightthickness=0)
        tempcanvas.place(relx=x, rely=y, anchor=CENTER)
        tempcanvas.create_oval(0,0,width,height, width=2, fill=color, outline=bordercolor)
        return tempcanvas


    def placerow(self, frame, colors, bgcolor, x, xstep, y, width, height, bind, start, end):
        '''Deze functie plaatst een hele lijst aan gekleurde rondjes op het scherm en kan
        ook nog een gegeven functie laten uitvoeren als je op een rondje drukt die deze functie
        maakt'''
        for ind in range(start, end):
            if colors[ind] == 'white':
                bordercolor = 'black'
            else:
                bordercolor = colors[ind]
            circle = self.placecolor(self, frame, colors[ind], bordercolor,
                                     bgcolor, x+(ind-start)*xstep, y, width, height)
            if bind is not None:
                circle.bind('<1>', bind(self, ind))


    def colorpick(self, frame, allcolors, bgcolor, title):
        '''Deze functie laat de mogelijke kleuren zien waarop de speler een keuze kan maken'''
        #deze variabele wordt gebruikt door de hoofdmodule om te detecteren of er een knop is ingedrukt
        CodeMaster.goVar = IntVar()
        choiceframe = CodeMaster.creategameframe(CodeMaster, frame, 400, RIGHT, 'white')
        #deze if statements kijkt of de kleuren voor de code weergegeven moeten worden of de
        #zwart/witte pinnen
        if len(allcolors) > 2:
            CodeMaster.code = []
            results = CodeMaster.code
        else:
            CodeMaster.pins = []
            results = CodeMaster.pins
        x = 0.3
        xstep = 0.2
        #deze for-loop zal ervoor zorgen dat de gegeven kleuren op rijen worden geplaatst niet groter dan 3
        for ind in range(0, len(allcolors), 3):
            endindex = ind+3
            #voorkomt dat er een indexerror komt voor lijsten die niet uit een veelvoud van 3 aantal
            #items bestaan
            if endindex > len(allcolors):
                endindex = len(allcolors)
            #deze if-statement kijkt of er een even aantal items in de lijst zitten en past zo de begin 'x' aan
            #om ervoor te zorgen dat deze nog steeds in het midden van het scherm staan
            if (endindex - ind) % 2 == 0:
                x += (xstep / 2)
            self.placerow(self, choiceframe, allcolors, bgcolor, x, xstep,
                          0.3 + ind/3*0.1, 50, 50,
                          lambda x, y:(lambda x:self.coloradd(x, y, choiceframe, allcolors, results)), ind, endindex)
        #de algemene titel en de knop voor het bevestigen van de keuze
        title = Label(choiceframe,
                      text=title,
                      font=('',15,'bold'),
                      bg=bgcolor)
        title.place(relx=0.5, rely=0.2, anchor=CENTER)
        confirm = Button(choiceframe,
                         text='Confirm',
                         bg='brown',
                         width=15,
                         height=2)
        confirm.place(relx=0.5, rely=0.6, anchor=CENTER)
        #de bevestigingsknop en frame die hiervoor gebruikt wordt worden gereturnd voor verder gebruik
        return confirm, choiceframe


    def coloradd(self, index, root, colors, result):
        '''Deze functie voegt een kleur toe aan het rijtje van gekozen kleuren'''
        #de lengte van de code kan maximaal 4 zijn
        if len(result) < 4:
            result.append(colors[index])
            CodeMaster.colorshow(CodeMaster, root, result)


    def colorshow(self, root, result):
        '''Deze functie geeft de gekozen kleuren weer'''
        #haalt frame weg en plaatst opnieuw, zodat weggehaalde kleuren verdwijnen
        try:
            self.colorframe.destroy()
        except AttributeError:
            pass
        #maakt frame opnieuw, zodat de huidige gekozen kleuren hierin geplaatst kunnen worden
        self.colorframe = Frame(root,
                           bg='white')
        self.colorframe.place(rely=0.7, height=100, width=400)
        self.placerow(self, self.colorframe, result, 'white', 0.15, 0.2, 0.5, 50, 50,
                      lambda x, y:(lambda x:self.colorremove(x, y, root, result)), 0, len(result))


    def colorremove(self, index, root, result):
        '''Deze functie verwijdert een kleur uit het rijtje van de gekozen kleuren'''
        result.pop(index)
        CodeMaster.colorshow(CodeMaster, root, result)


    def codeconfirm(self, frame, placeframe, background):
        '''Deze functie bevestigt het rijtje van gekozen kleuren voor de code'''
        #functie wordt alleen uitgevoerd als de code uit 4 kleuren bestaat
        if len(CodeMaster.code) == 4:
            frame.destroy()
            self.placerow(self, placeframe, CodeMaster.code, background, 0.2, 0.2, 0.92,
                          50, 50, None, 0, len(CodeMaster.code))
            CodeMaster.goVar.set(1)


    def pinconfirm(self, frame, placeframe, background, pins, totalguess, guessnumber):
        '''Deze functie haalt het scherm waar de pins geselecteerd kunnen worden weg en
        voert hierna een functie uit die de pinnen op het scherm plaatst'''
        frame.destroy()
        CodeMaster.goVar.set(1)
        self.showpins(self, placeframe, background, pins, totalguess, guessnumber)


    def showpins(self, placeframe, background, guess, totalguess, guessnumber):
        '''Deze functie laat de zwart/witte pinnen die als feedback voortkomen uit de code zien
        op het scherm'''
        for index in range(0, len(guess), 2):
            endindex = index + 2
            if endindex > len(guess):
                endindex = len(guess)
            self.placerow(self, placeframe, guess, background, 0.85, 0.08, guessnumber/totalguess*0.8-0.02+index*0.02,
                          15, 15, None, index, endindex)


    def showguess(self, frame, placeframe, background, colorguess, totalguess, guessnumber):
        '''Deze functie laat de kleuren zien die zijn geraden op het scherm'''
        if len(colorguess) == 4:
            if frame != None:
                frame.destroy()
            CodeMaster.goVar.set(1)
            self.placerow(self, placeframe, colorguess, background, 0.15, 0.16, guessnumber/totalguess*0.8,
                          40, 40, None, 0, len(colorguess))


    def showendmessage(self, root, text):
        '''Deze functie maakt een eindbericht als de game is afgelopen'''
        endmessage = Label(root,
                           text=text,
                           font=('', 15, 'bold'),
                           bg='white')
        endmessage.pack(side=RIGHT, padx=(0, 50))