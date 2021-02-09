from tkinter import *

# import Graphical_Interface
from Graphical_Interface import *


def startingscreen():
    root = startscreen.createscreen(startscreen, 400, 400,
                                    '', 'Mastermind', '#bd745d')
    buttons = startscreen.createbuttons(startscreen, root, 'brown', 15, 2, 0.12)
    buttons[0].configure(command=lambda: startscreen.gotoCMPlayer(startscreen, root))
    buttons[1].configure(command=lambda: startscreen.gotoCMComputer(startscreen, root))
    root.mainloop()
    return startscreen.playerchoice


def start():
    result = startingscreen()


if __name__ == '__main__':
    start()