from Tkinter import * 
from math import *	
from random import *
from PIL import ImageTk, Image

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
        text ='''----Presentation du jeu----
Le but du jeu est de trouver la combinaison magique choisie par l'ordinateur.
Selectionne parmis 6 couleurs puis l'ordinateur te dira, grace a des ronds noirs ou blancs la proximite avec la bonne combinaison.''').pack(padx =15, pady =10)

def deroule(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''WIP''').pack(padx =15, pady =10)

gagner=0
couleurs = ['red', 'blue', 'green','purple', 'orange', 'yellow']
cm1 =  choice(couleurs)
cm2 =  choice(couleurs)
cm3 =  choice(couleurs)
cm4 =  choice(couleurs)


couleurvariable='white'

def imageboite(): 
	can.create_image(250, 450, image=bkg)

def partie(interactioncouleur):
	can.delete(imageboite)
	can.create_oval(20, 30, 60, 70, fill='red', outline='white')#40 de diametre
	can.create_oval(20, 70, 60, 110, fill='green', outline='white')
	can.create_oval(20, 110, 60, 150, fill='blue', outline='white')
	can.create_oval(20, 150, 60, 190, fill='yellow', outline='white')
	can.create_oval(20, 190, 60, 230, fill='purple', outline='white')
	can.create_oval(20, 230, 60, 270, fill='orange', outline='white')

	can.create_oval(90, 30, 130, 70, fill=couleurvariable, outline='white')
	can.create_oval(90, 80, 130, 120, fill=couleurvariable, outline='white')
	can.create_oval(90, 130, 130, 170, fill=couleurvariable, outline='white')
	can.create_oval(90, 180, 130, 220, fill=couleurvariable, outline='white')
	can.create_oval(90, 230, 130, 270, fill=couleurvariable, outline='white')
	can.create_oval(90, 280, 130, 320, fill=couleurvariable, outline='white')
	can.create_oval(90, 330, 130, 370, fill=couleurvariable, outline='white')
	can.create_oval(90, 380, 130, 420, fill=couleurvariable, outline='white')

	can.create_oval(140, 30, 180, 70, fill='white', outline='white')
	can.create_oval(140, 80, 180, 120, fill='white', outline='white')
	can.create_oval(140, 130, 180, 170, fill='white', outline='white')
	can.create_oval(140, 180, 180, 220, fill='white', outline='white')
	can.create_oval(140, 230, 180, 270, fill='white', outline='white')
	can.create_oval(140, 280, 180, 320, fill='white', outline='white')
	can.create_oval(140, 330, 180, 370, fill='white', outline='white')
	can.create_oval(140, 380, 180, 420, fill='white', outline='white')

	can.create_oval(190, 30, 230, 70, fill='white', outline='white')
	can.create_oval(190, 80, 230, 120, fill='white', outline='white')
	can.create_oval(190, 130, 230, 170, fill='white', outline='white')
	can.create_oval(190, 180, 230, 220, fill='white', outline='white')
	can.create_oval(190, 230, 230, 270, fill='white', outline='white')
	can.create_oval(190, 280, 230, 320, fill='white', outline='white')
	can.create_oval(190, 330, 230, 370, fill='white', outline='white')
	can.create_oval(190, 380, 230, 420, fill='white', outline='white')

	can.create_oval(240, 30, 280, 70, fill='white', outline='white')
	can.create_oval(240, 80, 280, 120, fill='white', outline='white')
	can.create_oval(240, 130, 280, 170, fill='white', outline='white')
	can.create_oval(240, 180, 280, 220, fill='white', outline='white')
	can.create_oval(240, 230, 280, 270, fill='white', outline='white')
	can.create_oval(240, 280, 280, 320, fill='white', outline='white')
	can.create_oval(240, 330, 280, 370, fill='white', outline='white')
	can.create_oval(240, 380, 280, 420, fill='white', outline='white')

	can.create_oval(240, 480, 280, 520, fill='white', outline='white')
	can.create_oval(190, 480, 230, 520, fill='white', outline='white')
	can.create_oval(140, 480, 180, 520, fill='white', outline='white')
	can.create_oval(90, 480, 130, 520, fill='white', outline='white')
	can.create_text(180, 459, text="Solution",fill="white")

def nouvellePartie():
	can.delete(ALL)
	partie(interactioncouleur)
def interactioncouleur(event):
	x,y = event.x,event.y
	if x>20 & x<60 :
		couleurvariable='red'
		can.create_oval(90, 30, 130, 70, fill=couleurvariable, outline='white')
def montrercombinaisonmagique():
	can.create_oval(240, 480, 280, 520, fill=cm1, outline='white')
	can.create_oval(190, 480, 230, 520, fill=cm2, outline='white')
	can.create_oval(140, 480, 180, 520, fill=cm3, outline='white')
	can.create_oval(90, 480, 130, 520, fill=cm4, outline='white')

def menu(win):
    "Barre de menu"
    top=Menu(win)
    win.config(menu=top)
    J=Menu(top)
    top.add_cascade(label='Jeu',menu=J,underline=0)
    J.add_command(label='Nouvelle partie',command=nouvellePartie,underline=0)
    R=Menu(top)
    top.add_cascade(label='Regles',menu=R,underline=0)
    R.add_command(label='Presentation',command=presentation,underline=0)
    R.add_command(label='Deroule',command=deroule,underline=0)
    O=Menu(top)
    top.add_cascade(label='Options',menu=O,underline=0)
    O.add_command(label='A propos',command=aPropos,underline=0)
    O.add_command(label='Quitter le jeu',command=quitter,underline=0)

def gagne():
	gagner=1
	can.create_text(400, 600, text="Bravo ! Tu as trouve la combinaison !",fill="white")
	montrercombinaisonmagique()

def quitter(): 
    ans=askokcancel('KINGMIND',"Vraiment , On fait la belle ?") 
    if ans:
	fenetre.quit()

clicsouris=0

def mouseDown( event):
	X,Y=event.x,event.y
	if X==(20,60)&Y==(30,70):
		rouge=1
		if X==(25,100):
			can.create_oval(90, 30, 130, 70, fill='red', outline='white')

def mouseUp( event):
    global selObject,clicsouris
    if clicsouris==1: #si la fonction <clic> de la souris est activee...
        can.itemconfig(selObject,width=2) # le contour de l'objet selectionne revient a son epaisseur initiale
    if clicsouris==0: #si la fonction <clic> de la souris n'est pas activee...
        selObject=None
fenetre=Tk()
fenetre.title('KingMind Alpha build') 
menu(fenetre)
bkg = PhotoImage(file='bkg.gif')
can=Canvas(fenetre,height=800,width=500, bg='black') 
can.grid(row=0,column=0)
fenetre.bind("<Button-1>", ) # commandes avec le clic gauche de la souris, lorsqu'il est enfonce
fenetre.bind("<Button1-ButtonRelease>", mouseUp)
imageboite()

fenetre.config(bg="black") 
fenetre.mainloop()
fenetre.destroy() 
