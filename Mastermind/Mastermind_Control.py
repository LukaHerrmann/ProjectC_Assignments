from tkinter import *

import Graphical_Interface

root = Graphical_Interface.startscreen.createscreen(Graphical_Interface.startscreen, 400, 400, '#bd745d')
buttons = Graphical_Interface.startscreen.createbuttons(Graphical_Interface.startscreen, root, 'brown', 15, 2, 0.15)
root.mainloop()
