from tkinter import *



class startscreen():
    def createscreen(self, windowwidth, windowheight, bgcolor):
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


class CMComputer():
    pass


class CMPlayer():
    pass