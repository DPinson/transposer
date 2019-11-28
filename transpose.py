"""Auteur: Denis Pinson
   Date : 28/11/2019
   But du programme : transposer un texte en décalant les lettres, consonne vers consonne et voyelle vers voyelle 
   Entrée: le texte à modifier (exemple : Hello World)
   Sorties: le texte donc les lettres ont été décalées (exemple : Konny Zytng)
"""
import tkinter

FRANCAIS = 0
ANGLAIS = 1
ARABE = 2

app = tkinter.Tk()
app.geometry("500x500")
app.title("Transposer un texte")

def updateLabel(*args):
    message = texteBase.get()
    nouveauTexte = ""
    for i in range(len(message)) : 
        nouveauTexte += transposerAnglais(message[i])
        i =+ 1
    varTexteNouveau.set(nouveauTexte)

def defineLang(*args) :
    #varLang.set()
    pass

def transposerAnglais(lettre) : 
    voyelle = ["a", "e", "i", "o", "u", "y"]
    consonne = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    if lettre in voyelle :
        nouvellelettre = voyelle.index(lettre) + 2
        return voyelle[nouvellelettre]
    elif lettre in consonne : 
        nouvellelettre = consonne.index(lettre) + 2
        return consonne[nouvellelettre]
    else :
        return lettre

varTexteBase = tkinter.StringVar()
varTexteBase.trace("w", updateLabel)
texteBase = tkinter.Entry(app, textvariable = varTexteBase)

varTexteNouveau = tkinter.StringVar()
texteNouveau = tkinter.Entry(app, textvariable = varTexteNouveau)

texteBase.pack()
texteNouveau.pack()

app.mainloop()