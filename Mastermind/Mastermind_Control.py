from tkinter import *

# import Graphical_Interface
from Graphical_Interface import *
import CodeMaster_Computer

background = '#bd745d'
allcolors = ['black', 'lime', 'orange', 'red', 'blue', 'yellow']


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
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, LEFT, background)
    code = CodeMaster_Computer.makecode(allcolors, 4)
    choiceframe = CodeMaster.creategameframe(CodeMaster, root, 400, RIGHT, 'white')
    confirm = CodeMaster.colorpick(CodeMaster, choiceframe, allcolors, 'white', 'Guess a code')
    confirm.configure(command=lambda: CodeMaster.showguess(CodeMaster, gameframe, background, CodeMaster.code,
                                                           8, 1))
    print(CodeMaster_Computer.determinepins(code, ['black', 'white', 'black', 'blue']))
    root.mainloop()


def cmplayer():
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, LEFT, background)
    choiceframe = CodeMaster.creategameframe(CodeMaster, root, 400, RIGHT, 'white')
    guessframe = CodeMaster.creategameframe(CodeMaster, root, 400, RIGHT, 'white')
    confirm = CodeMaster.colorpick(CodeMaster, choiceframe, allcolors,
                                   'white', 'Pick four colors for the code')
    confirm.configure(command=lambda: CodeMaster.codeconfirm(CodeMaster, choiceframe, gameframe,
                                                             guessframe, background))
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