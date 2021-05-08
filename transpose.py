"""Author: Denis Pinson
   Date : 16/05/2020
   Goal : to change a text letter by letter, consonant to consonant and voyel to voyel, in a different order
   you can choose between 3 languages
   in: the text you want to change (exemple : Hello World)
   out: the new changed text (exemple : Byffe Qelfw)
"""
import tkinter as tk
import transposerLanguage as tL

# Language constants to choose starting language and which changes to make
FRANCAIS = 1
ENGLISH = 0
ARABIAN = 2

class Transpose():
    """Where you can find the function to change the text to the new version
    """ 

    def changeText(self, *args):
        """ 
        This function return the new text
        """
        message = base_text.get()
        new_text = ""
        lang = var_lang.get()
        for i in range(len(message)): 
            if lang == ENGLISH:
                new_text += tL.transposerEnglish(message[i])
            elif lang == FRANCAIS: 
                new_text += tL.transposerFrancais(message[i])
            else:
                new_text += tL.transposerArabian(message[i])
            i =+ 1
        var_new_text.set(new_text)


transposer = tk.Tk()
transposer.wm_state('zoomed') # for full screen
transposer.configure(bg="lightgreen")
transposer.positionfrom("user")
transposer.title("Transposer un texte")


page = tk.LabelFrame(transposer, border=0, background="lightgreen", text="Appli pour transposer du texte")

choose_lang = tk.LabelFrame(page, width=20, background="lightgreen", text="Choisissez votre langue de départ")

var_lang = tk.IntVar()
radioEnglish = tk.Radiobutton(choose_lang, text="Anglais", value=ENGLISH, variable=var_lang, background="lightgreen", width="10")
radioFrancais = tk.Radiobutton(choose_lang, text="Français", value=FRANCAIS, variable=var_lang, background="lightgreen", width="10")
radioArabian = tk.Radiobutton(choose_lang, text="Arabe", value=ARABIAN, variable=var_lang, background="lightgreen", width="10")

entries = tk.LabelFrame(page, background="lightgreen", text="Entrer un texte à transcoder")
var_base_text = tk.StringVar() 
var_base_text.trace("w", Transpose.changeText)
base_text = tk.Entry(entries, textvariable = var_base_text)

outsees = tk.LabelFrame(page, background="lightgreen", text="Voici le texte modifié")
var_new_text = tk.StringVar()
new_text = tk.Entry(outsees, textvariable = var_new_text)

page.pack(fill=tk.BOTH)

outsees.pack(fill=tk.X, side="bottom")
new_text.pack(fill=tk.X)
entries.pack(fill=tk.X, side="bottom")
base_text.pack(fill=tk.X)
choose_lang.pack(side="left")
radioArabian.pack()
radioFrancais.pack()
radioEnglish.pack()

transposer.mainloop()