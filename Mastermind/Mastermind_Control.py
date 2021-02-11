from tkinter import *

from Graphical_Interface import *
from CodeMaster import CodeMaster_Player
from CodeMaster import CodeMaster_Computer

maxguesses = 8
background = '#bd745d'
allcolors = ['black', 'lime', 'orange', 'red', 'blue', 'yellow']
pins = ['black', 'white']
possiblecases = ((0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (4,0))


def startingscreen():
    '''Deze functie maakt een grafische interface waarbij de speler kan kiezen of hij/zij de codemaster
    wil zijn of wil dat de computer de codemaster is'''
    root = startscreen.createscreen(startscreen, 400, 400,
                                    '', 'Mastermind', '#bd745d')
    buttons = startscreen.createbuttons(startscreen, root, 'brown', 15, 2, 0.12)
    buttons[0].configure(command=lambda: startscreen.gotoCMComputer(startscreen, root))
    buttons[1].configure(command=lambda: startscreen.gotoCMPlayer(startscreen, root))
    root.mainloop()
    return startscreen.playerchoice


def cmcomputer():
    '''Deze functie maakt de grafische interface en verzorgt de algoritmes als de computer de code moet
    maken en de speler deze moet raden'''
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
            CodeMaster.showendmessage(CodeMaster, root, 'You won :)')
            break
    else:
        CodeMaster.showendmessage(CodeMaster, root, 'You lost :(')
        CodeMaster.placerow(CodeMaster, gameframe, code, background, 0.2, 0.2, 0.92,
                      50, 50, None, 0, len(code))
    root.mainloop()


def cmplayer():
    '''Deze functie maakt de grafische interface en verzorgt de algoritmes als de computer de code
    van de speler moet raden'''
    possibilities = CodeMaster_Player.getpossiblecombinations(CodeMaster_Player, '012345')
    root = startscreen.createscreen(startscreen, 800, 700, 'Mastermind', '', 'white')
    gameframe = CodeMaster.creategameframe(CodeMaster, root, 400, LEFT, background)
    confirm = CodeMaster.colorpick(CodeMaster, root, allcolors,
                                   'white', 'Pick four colors for the code')
    confirm[0].configure(command=lambda: CodeMaster.codeconfirm(CodeMaster,root, confirm[1], gameframe, background,
                                                                maxguesses, 1))
    confirm[0].wait_variable(CodeMaster.goVar)
    for round in range(1, maxguesses+1):
        if len(possibilities) == 0:
            CodeMaster.showendmessage(CodeMaster, root, 'You chose the pins wrong >:(')
            break
        #de simple algorithm
        # computerguesscode = CodeMaster_Player.simplestrategy(CodeMaster_Player, possibilities)
        #de expected value algorithm
        # computerguesscode = CodeMaster_Player.expectedsizestrategy(CodeMaster_Player, possibilities, possiblecases)
        #eigen algorithm
        computerguesscode = CodeMaster_Player.ownstrategy(CodeMaster_Player, possibilities)
        computerguesscolor = CodeMaster_Player.numbtocolor(CodeMaster_Player, computerguesscode, allcolors)
        confirm = CodeMaster.colorpick(CodeMaster, root, pins, 'white', 'Pick the correct pins')
        #confirm[0] is een knop die de functie aanmaakt en comfirm[1] is een frame die de functie maakt
        confirm[0].configure(command=lambda: CodeMaster.pinconfirm(CodeMaster, confirm[1], gameframe, background,
                                                                   CodeMaster.pins, maxguesses, round))
        #geeft de gok op het scherm weer
        CodeMaster.showguess(CodeMaster, None, gameframe, background, computerguesscolor, maxguesses, round)
        confirm[0].wait_variable(CodeMaster.goVar)
        feedback = CodeMaster_Player.getfeedback(CodeMaster_Player, CodeMaster.pins)
        #bij deze feedback zijn alle kleuren goed
        if feedback == (4, 0):
            CodeMaster.showendmessage(CodeMaster, root, 'You lost :(')
            break
        possibilities = CodeMaster_Player.newposibilities(CodeMaster_Player, possibilities, computerguesscode, feedback)
    else:
        CodeMaster.showendmessage(CodeMaster, root, 'You won :)')

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