from tkinter import *

# import Graphical_Interface
from Graphical_Interface import *
import CodeMaster_Computer
import CodeMaster_Player

maxguesses = 8
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
    for round in range(1, maxguesses+1):
        confirm = CodeMaster.colorpick(CodeMaster, root, allcolors, 'white', 'Guess a code')
        confirm[0].configure(command=lambda: CodeMaster.showguess(CodeMaster, confirm[1], root, gameframe, background, CodeMaster.code,
                                                               allcolors, maxguesses, round))
        confirm[0].wait_variable(CodeMaster.goVar)
        pins = CodeMaster_Computer.determinepins(code, CodeMaster.code)
        CodeMaster.showpins(CodeMaster, gameframe, background, pins, maxguesses, round)
        if pins == ['black' for x in range(4)]:
            result = Label(root,
                           text='You won :)',
                           font=('', 15, 'bold'),
                           bg='white')
            result.pack(side=RIGHT, padx=(0, 50))
            break
    else:
        result = Label(root,
                       text='You lost :(',
                       font=('',15,'bold'),
                       bg='white')
        result.pack(side=RIGHT,padx=(0,50))
        CodeMaster.placerow(CodeMaster, gameframe, code, background, 0.2, 0.2, 0.92,
                      50, 50, None, 0, len(code))
    root.mainloop()


def cmplayer():
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, LEFT, background)
    confirm = CodeMaster.colorpick(CodeMaster, root, allcolors,
                                   'white', 'Pick four colors for the code')
    confirm[0].configure(command=lambda: CodeMaster.codeconfirm(CodeMaster,root, confirm[1], gameframe, background,
                                                                maxguesses, 1))
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
    CodeMaster_Player.getpossiblecombinations('012345')