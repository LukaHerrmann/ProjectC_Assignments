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


    def placerow(self, frame, colors, bgcolor, x, xstep, y, width, height):
        for ind in range(len(colors)):
            self.placecolor(self, frame, colors[ind], bgcolor, x+ind*xstep, y, width, height)


    def colorpick(self, frame, allcolors, bgcolor):
        for ind in range(0, len(allcolors), 3):
            self.placerow(self, frame, allcolors[ind:ind+3], bgcolor, 0.25, 0.2, 0.3 + ind/3*0.1, 50, 50)
        title = Label(frame,
                      text='Pick four colors',
                      font=('',15,'bold'),
                      bg=bgcolor)
        title.place(relx=0.5, rely=0.2, anchor=CENTER)
        confirm = Button(frame,
                         text='Confirm',
                         bg='brown',
                         width=15,
                         height=2)
        confirm.place(relx=0.5, rely=0.6, anchor=CENTER)