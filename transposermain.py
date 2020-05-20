"""Author: Denis Pinson
   Date : 16/05/2020
   Goal : to change a text letter by letter, consonant to consonant and voyel to voyel, in a different order
   you can choose between 3 languages, French, English and Arabian (classical)
   in: the text you want to change (exemple : Hello World)
   out: the new changed text (exemple : Byffe Qelfw)
"""
import tkinter as tk
from transpose import Transpose

transposer = tk.Tk()
transposer.wm_state('zoomed') # for full screen
transposer.configure(bg="lightgreen")
transposer.positionfrom("user")
transposer.title("Transposer un texte")

page = Transpose(transposer)
page.pack(fill=tk.BOTH)

transposer.mainloop()