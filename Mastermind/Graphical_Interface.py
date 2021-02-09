from tkinter import *



class startscreen():
    def __init__(self):
        root = self.createscreen(400, 400, '#bd745d')
        root.mainloop()


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


class CMComputer():
    pass


class CMPlayer():
    pass