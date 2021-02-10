from tkinter import *



class startscreen():
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
        ''''''
        #playerchoice is False als de gebruiker wil dat de computer de codemaster is
        startscreen.playerchoice = False
        root.destroy()


    def gotoCMPlayer(self, root):
        ''''''
        #playerchoice is True als de gebruiker de codemaster wil zijn
        startscreen.playerchoice = True
        root.destroy()


class CodeMaster():
    code = []
    pins = []
    step = 1
    def creategameframe(self, root, width, side, bgcolor):
        mastergame = Frame(root,
                           width=width,
                           bg=bgcolor)
        mastergame.pack(side=side, fill=Y, expand=True, anchor='w')
        return mastergame


    def placecolor(self, frame, color, bordercolor, bgcolor, x, y, width, height):
        tempcanvas = Canvas(frame,
                            bg=bgcolor,
                            width=width,
                            height=height,
                            highlightthickness=0)
        tempcanvas.place(relx=x, rely=y, anchor=CENTER)
        tempcanvas.create_oval(0,0,width,height, fill=color, outline=bordercolor)
        return tempcanvas


    def placerow(self, frame, colors, bgcolor, x, xstep, y, width, height, bind, start, end):
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
        CodeMaster.goVar = IntVar()
        choiceframe = CodeMaster.creategameframe(CodeMaster, frame, 400, RIGHT, 'white')
        if len(allcolors) > 2:
            CodeMaster.code = []
            results = CodeMaster.code
        else:
            CodeMaster.pins = []
            results = CodeMaster.pins
        x = 0.3
        xstep = 0.2
        for ind in range(0, len(allcolors), 3):
            endindex = ind+3
            if endindex > len(allcolors):
                endindex = len(allcolors)
            if (endindex - ind) % 2 == 0:
                x += (xstep / 2)
            self.placerow(self, choiceframe, allcolors, bgcolor, x, xstep,
                          0.3 + ind/3*0.1, 50, 50,
                          lambda x, y:(lambda x:self.coloradd(x, y, choiceframe, allcolors, results)), ind, endindex)
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
        return confirm, choiceframe


    def coloradd(self, index, root, colors, result):
        if len(result) < 4:
            result.append(colors[index])
            CodeMaster.colorshow(CodeMaster, root, result)


    def colorshow(self, root, result):
        try:
            self.colorframe.destroy()
        except AttributeError:
            pass
        self.colorframe = Frame(root,
                           bg='white')
        self.colorframe.place(rely=0.7, height=100, width=400)
        self.placerow(self, self.colorframe, result, 'white', 0.15, 0.2, 0.5, 50, 50,
                      lambda x, y:(lambda x:self.colorremove(x, y, root, result)), 0, len(result))


    def colorremove(self, index, root, result):
        result.pop(index)
        CodeMaster.colorshow(CodeMaster, root, result)


    def codeconfirm(self, root, frame, placeframe, background, totalguess, guessnumber):
        if len(CodeMaster.code) == 4:
            frame.destroy()
            self.placerow(self, placeframe, CodeMaster.code, background, 0.2, 0.2, 0.92,
                          50, 50, None, 0, len(CodeMaster.code))
            CodeMaster.goVar.set(1)


    def pinconfirm(self, frame, placeframe, background, pins, totalguess, guessnumber):
        frame.destroy()
        CodeMaster.goVar.set(1)
        self.showpins(self, placeframe, background, pins, totalguess, guessnumber)


    def showpins(self, placeframe, background, guess, totalguess, guessnumber):
        for index in range(0, len(guess), 2):
            endindex = index + 2
            if endindex > len(guess):
                endindex = len(guess)
            self.placerow(self, placeframe, guess, background, 0.85, 0.08, guessnumber/totalguess*0.8-0.02+index*0.02,
                          15, 15, None, index, endindex)


    def showguess(self, frame, placeframe, background, colorguess, totalguess, guessnumber):
        if len(colorguess) == 4:
            if frame != None:
                frame.destroy()
            CodeMaster.goVar.set(1)
            self.placerow(self, placeframe, colorguess, background, 0.15, 0.16, guessnumber/totalguess*0.8,
                          40, 40, None, 0, len(colorguess))