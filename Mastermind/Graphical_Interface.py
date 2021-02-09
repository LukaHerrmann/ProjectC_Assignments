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
                                    text='Raad de code',
                                    bg=buttoncolor,
                                    width=width,
                                    height=height)
        codemastercomputer.place(relx=0.5, rely=0.5-spacing, anchor=CENTER)
        codemasterplayer = Button(root,
                                  text='Bepaal de code',
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
    allcolors = ['black', 'lime', 'orange', 'red', 'blue', 'yellow']
    code = []
    def creategameframe(self, root, width, side, bgcolor):
        mastergame = Frame(root,
                           width=width,
                           bg=bgcolor)
        mastergame.pack(side=side, fill=Y, expand=True)
        return mastergame


    def placecolor(self, frame, color, bgcolor, x, y, width, height):
        tempcanvas = Canvas(frame,
                            bg=bgcolor,
                            width=width,
                            height=height,
                            highlightthickness=0)
        tempcanvas.place(relx=x, rely=y)
        tempcanvas.create_oval(0,0,width,height, fill=color, outline=color)
        return tempcanvas


    def placerow(self, frame, colors, bgcolor, x, xstep, y, width, height, bind, start, end):
        index = 0
        for ind in range(start, end):
            circle = self.placecolor(self, frame, colors[ind], bgcolor, x+index*xstep, y, width, height)
            if bind is not None:
                circle.bind('<1>', bind(self, ind))
            index += 1



    def colorpick(self, frame, allcolors, bgcolor, title):
        for ind in range(0, len(allcolors), 3):
            self.placerow(self, frame, allcolors, bgcolor, 0.25, 0.2,
                          0.3 + ind/3*0.1, 50, 50, lambda x, y:(lambda x:self.coloradd(x, y, frame)), ind, ind+3)
        title = Label(frame,
                      text='Pick four colors {}'.format(title),
                      font=('',15,'bold'),
                      bg=bgcolor)
        title.place(relx=0.5, rely=0.2, anchor=CENTER)
        confirm = Button(frame,
                         text='Confirm',
                         bg='brown',
                         width=15,
                         height=2)
        confirm.place(relx=0.5, rely=0.6, anchor=CENTER)


    def coloradd(self, index, root):
        if len(CodeMaster.code) < 4:
            CodeMaster.code.append(CodeMaster.allcolors[index])
            CodeMaster.colorshow(CodeMaster, root)


    def colorshow(self, root):
        try:
            self.colorframe.destroy()
        except AttributeError:
            pass
        self.colorframe = Frame(root,
                           bg='white')
        self.colorframe.place(rely=0.7, height=100, width=400)
        self.placerow(self, self.colorframe, CodeMaster.code, 'white', 0.15, 0.2, 0.5, 50, 50,
                      lambda x, y:(lambda x:self.colorremove(x, y, root)), 0, len(CodeMaster.code))


    def colorremove(self, index, root):
        CodeMaster.code.pop(index)
        CodeMaster.colorshow(CodeMaster, root)