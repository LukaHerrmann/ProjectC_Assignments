from tkinter import *

# import Graphical_Interface
from Graphical_Interface import *

background = '#bd745d'


def startingscreen():
    root = startscreen.createscreen(startscreen, 400, 400,
                                    '', 'Mastermind', '#bd745d')
    buttons = startscreen.createbuttons(startscreen, root, 'brown', 15, 2, 0.12)
    buttons[0].configure(command=lambda: startscreen.gotoCMComputer(startscreen, root))
    buttons[1].configure(command=lambda: startscreen.gotoCMPlayer(startscreen, root))
    root.mainloop()
    return startscreen.playerchoice


def cmcomputer():
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, '#bd745d')
    root.mainloop()


def cmplayer():
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, background)
    CodeMaster.placerow(CodeMaster, gameframe, ['red', 'blue', 'yellow', 'black'], background, 0.05, 50, 50)
    root.mainloop()


def start():
    # result is True als de gebruiker de codemaster wil zijn en False als de gebruiker
    # wil dat de computer code master is
    result = startingscreen()
    if result != None:
        if result:
            cmplayer()
        else:
            cmcomputer()


if __name__ == '__main__':
    start()