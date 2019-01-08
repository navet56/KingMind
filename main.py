#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import * 
from math import *	
from random import *
from PIL import ImageTk, Image
from tkMessageBox import  askokcancel

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']        # Liste des couleurs disponibles
finalList = [0, 0, 0, 0]        # Liste = La combinaison de couleurs à deviner
currentList = [0, 0, 0, 0]
cercleCoord = []        # Liste, de listes  = coordonnées des 4 cercles, d'un essai   
nbClic = 0        # gestion du nombre de "clic gauche souris", utilisée pour sélectionner une couleur
num = 1
jouer = False
def aPropos(): 
    msg =Toplevel() 
    Message(msg, width=200, aspect=200, justify=CENTER, 
        text ='''KingMind
Par Evan Diberder, Mael Le Boulicaut, Kilian Buan et Julian Goumida
Tk version 8.4
Python 2.7
License GNU GPL V3
Version Alpha 0.2''').pack(padx =15, pady =10)

def imageboite(): 
	plateau.create_image(200, 350, image=bkg)

def presentation(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =150, justify =CENTER, 
        text ='''----Presentation du jeu----
Le but du jeu est de trouver la combinaison magique choisie par l'ordinateur.
Selectionne parmis 6 couleurs puis l'ordinateur te dira, grace a des ronds rouges ou blancs la proximite avec la bonne combinaison.''').pack(padx =15, pady =10)

def deroule(): 
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''WIP''').pack(padx =15, pady =10)
def menu(fenetre):
    "Barre de menu"
    top=Menu(fenetre)
    fenetre.config(menu=top)
    J=Menu(top)
    top.add_cascade(label='Jeu',menu=J,underline=0)
    J.add_command(label='Nouvelle partie',command=jouer,underline=0)
    J.add_command(label='Essai',command=nouvelessai,underline=0)
    R=Menu(top)
    top.add_cascade(label='Regles',menu=R,underline=0)
    R.add_command(label='Presentation',command=presentation,underline=0)
    R.add_command(label='Deroule',command=deroule,underline=0)
    O=Menu(top)
    top.add_cascade(label='Options',menu=O,underline=0)
    O.add_command(label='A propos',command=aPropos,underline=0)
    O.add_command(label='Quitter le jeu',command=quitter,underline=0)

def tirage():
        """ Tirage de la combinaison de couleur à deviner + Mise en forme: suite de 5 couleurs à deviner """
        plateau.create_rectangle(10, 8, 190, 42, outline='white',fill='black')
        for i in range (4):
                finalList[i] = choice(colorList)        # tirage au sort d'une couleur dans la liste: colorList[]
                # Tracé d'un rectangle et des cercles représentant la combinaison à rechercher
                plateau.create_oval ((i+1)*40-15, 10, (i+1)*40+15, 40, outline = "black")
                txt = plateau.create_text((i+1)*40, 25, text="?", font="Arial 16 ", fill="blue")
        
        
def reveal():
        """ Pour révéler la suite recherchée... """ 
        for i in range (len(finalList)):
                plateau.create_oval ((i+1)*40-15, 10, (i+1)*40+15, 40, fill = finalList[i])
                
def color(event):
        """ Gestion de l'événement "Clic gauche", sur un cercle, pour sélectionner une couleur """
    
        global nbClic
        if nbClic >= 6: nbClic = 0
        # position du pointeur de la souris:
        X = event.x
        Y = event.y
        # Identification du cercle "cliqué" + sélection d'une couleur
	for i in range (4):
        	if (cercleCoord [i][0] <= X <= cercleCoord [i][2]) and (cercleCoord [i][1] <= Y <= cercleCoord [i][3]):
                	plateau.create_oval (cercleCoord[i], fill = colorList[nbClic])
                        currentList[i] = nbClic
        nbClic = nbClic+1        
def jouer():
        """ Gestion du jeu: le clic sur le bouton "essai", déclenche l'évaluation de la combinaison proposée"""
        # Mise en place du bouton "essai N°":
        """ C'est à partir de l'ACTION sur ce bouton qu'il faut continuer le MOTEUR DU JEU """
        plateau.delete(ALL)
	choiceColor(num)        # appelle la mise en place des cercles qui seront colorés par: color(event)
	tirage()
	jouer = True


def nouvelessai():
	global num
	print(bool(jouer))
	#if jouer == True: #and finalList[]==colorList[]:
        num = num+1
	choiceColor(num)
        for i in range (4):
            print("Comparaison essai :")
            print(currentList[i] == finalList[i])
def choiceColor(num):
        """ Mise en place des cercles de la proposition, avant leur coloration"""
        for i in range (4):
                # mise en place cercles
                cercle = plateau.create_oval ((i+1)*40-15, num*70-15, (i+1)*40+15, num*70+15, outline = "white")
                
                cercleCoord.insert (i, plateau.coords (cercle))        # Récupère les coordonnées des cercles
def quitter(): 
    reponse=askokcancel('KingMind',"Tu veux vraiment quitter ? On fait pas la belle ?") 
    if reponse:
        fenetre.quit() 
                       
##### PROGRAMME PRINCIPAL #####
        
fenetre= Tk()
fenetre.title('KingMind 0.2')
plateau = Canvas(fenetre, height =700,width=400, bg = 'black' )
plateau.pack(side =RIGHT, padx =0, pady =0)
essaiBouton = Button(fenetre, text = ("Essai"), command =nouvelessai)        
essaiBouton.pack(side=TOP, padx=0, pady=0)
menu(fenetre)
bkg = PhotoImage(file='bkg.gif')
imageboite()
# La méthode bind() permet de lier un événement avec une fonction
plateau.bind('<Button-1>',color)

fenetre.mainloop()
