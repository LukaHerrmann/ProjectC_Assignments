from tkinter import *

from Graphical_Interface import *
from CodeMaster import CodeMaster_Player
from CodeMaster import CodeMaster_Computer

maxguesses = 8
background = '#bd745d'
allcolors = ['black', 'lime', 'orange', 'red', 'blue', 'yellow']
pins = ['black', 'white']


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
    code = CodeMaster_Computer.makecode(CodeMaster_Computer, allcolors, 4)
    for round in range(1, maxguesses+1):
        confirm = CodeMaster.colorpick(CodeMaster, root, allcolors, 'white', 'Guess a code')
        confirm[0].configure(command=lambda: CodeMaster.showguess(CodeMaster, confirm[1], gameframe, background,
                                                                  CodeMaster.code, maxguesses, round))
        confirm[0].wait_variable(CodeMaster.goVar)
        pincolors = CodeMaster_Computer.determinepins(CodeMaster_Computer, code, CodeMaster.code)
        pins = CodeMaster_Computer.feedbacktocolor(CodeMaster_Computer, pincolors)
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
    possibilities = CodeMaster_Player.getpossiblecombinations(CodeMaster_Player, '012345')
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, LEFT, background)
    confirm = CodeMaster.colorpick(CodeMaster, root, allcolors,
                                   'white', 'Pick four colors for the code')
    confirm[0].configure(command=lambda: CodeMaster.codeconfirm(CodeMaster,root, confirm[1], gameframe, background,
                                                                maxguesses, 1))
    confirm[0].wait_variable(CodeMaster.goVar)
    code = CodeMaster_Player.colortonumb(CodeMaster_Player, CodeMaster.code, allcolors)
    for round in range(1, maxguesses+1):
        if len(possibilities) == 0:
            result = Label(root,
                           text='You chose the pins wrong >:(',
                           font=('', 15, 'bold'),
                           bg='white')
            result.pack(side=RIGHT, padx=(0, 50))
            break
        computerguesscolor = CodeMaster_Player.numbtocolor(CodeMaster_Player, possibilities[0], allcolors)
        computerguesscode = CodeMaster_Player.colortonumb(CodeMaster_Player, computerguesscolor, allcolors)
        confirm = CodeMaster.colorpick(CodeMaster, root, pins, 'white',
                                       'Pick the correct pins')
        confirm[0].configure(command=lambda: CodeMaster.pinconfirm(CodeMaster, confirm[1], gameframe, background,
                                                                   CodeMaster.pins, maxguesses, round))
        CodeMaster.showguess(CodeMaster, None, gameframe, background, computerguesscolor, maxguesses, round)
        confirm[0].wait_variable(CodeMaster.goVar)
        feedback = CodeMaster_Player.getfeedback(CodeMaster_Player, CodeMaster.pins)
        if feedback == (4, 0):
            result = Label(root,
                           text='You lost :(',
                           font=('', 15, 'bold'),
                           bg='white')
            result.pack(side=RIGHT, padx=(0, 50))
            break
        possibilities = CodeMaster_Player.newposibilities(CodeMaster_Player, possibilities, computerguesscode, feedback)
    else:
        result = Label(root,
                       text='You won :)',
                       font=('', 15, 'bold'),
                       bg='white')
        result.pack(side=RIGHT, padx=(0, 50))

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