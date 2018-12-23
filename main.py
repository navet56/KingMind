from Tkinter import * 
from math import *	
from random import randrange
from tkMessageBox import askokcancel 

def aPropos(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =200, justify =CENTER, 
        text ='''KingMind
Par Evan Diberder, Mael Le Boulicaut, Kilian Buan et Julian Goumida
Tk version 8.4
Python 2.7
License GNU GPL V3
Version Alpha 0.1''').pack(padx =15, pady =10)

def presentation(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''WIP''').pack(padx =15, pady =10)

def deroule(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''WIP''').pack(padx =15, pady =10)

def menu(win):
    "Barre de menu"
    top=Menu(win)
    win.config(menu=top)
    J=Menu(top)
    top.add_cascade(label='Jeu',menu=J,underline=0)
    J.add_command(label='Nouvelle partie'),#command=nouvellePartie,underline=0)
    R=Menu(top)
    top.add_cascade(label='Regles',menu=R,underline=0)
    R.add_command(label='Presentation',command=presentation,underline=0)
    R.add_command(label='Deroule',command=deroule,underline=0)
    O=Menu(top)
    top.add_cascade(label='Options',menu=O,underline=0)
    O.add_command(label='A propos',command=aPropos,underline=0)
    O.add_command(label='Quitter le jeu',command=quitter,underline=0)

def quitter(): 
	fenetre.quit()

fenetre=Tk()
fenetre.title('KingMind Alpha build') 
menu(fenetre)

can=Canvas(fenetre,height=800,width=600, bg='dark green') 
can.grid(row=1,column=0)

fenetre.config(bg="brown") 
fenetre.mainloop()
fenetre.destroy() 
