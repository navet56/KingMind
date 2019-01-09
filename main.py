#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
from math import *      
from random import *
#from PIL import ImageTk, Image
from tkinter.messagebox import  askokcancel

idColorList = [0, 1, 2, 3, 4, 5]
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']        # Liste des couleurs disponibles
finalList = [0, 0, 0, 0]                                                  # Liste = La combinaison de couleurs à deviner
currentList = [0, 0, 0, 0]                                                # Liste = Couleurs choisies par l joueur
cercleCoord = []                                                          # Liste, de listes  = coordonnées des 4 cercles, d'un essai   
nbClic = 0                                                                # gestion du nombre de "clic gauche souris", utilisée pour sélectionner une couleur
num = 1
jouant = False
def aPropos():         #Création de la section "à propos"             
    msg =Toplevel() 
    Message(msg, width=200, aspect=200, justify=CENTER, 
        text ='''KingMind
Par Evan Diberder, Mael Le Boulicaut, Kilian Buan
Tk version 8.4
Python 2.7
License GNU GPL V3
Version Alpha 0.2''').pack(padx =15, pady =10)

#def imageboite(): 
#        plateau.create_image(200, 350, image=bkg)

def presentation():    #Création de la section "présentation"
    msg =Toplevel() 
    Message(msg, width =200, aspect =150, justify =CENTER, 
        text ='''----Presentation du jeu----
Le but du jeu est de trouver la combinaison magique choisie par l'ordinateur.
Selectionne parmis 6 couleurs puis l'ordinateur te dira, grace a des ronds rouges ou blancs la proximite avec la bonne combinaison.''').pack(padx =15, pady =10)

def deroule():         #Création de la section "déroule"
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''----Comment jouer à KingMind----
Pour changer les couleurs, il faut cliquer sur les 4 cercles qui vous sont présentés.
Pour voir si votre combinaison est la bonne, il faut cliquer sur le bouton essai en haut à gauche.
A chaque essai, 4 points de couleur rouges ou blancs vous sont présentés :
Les Rouges correspondent à une bonne couleur à la bonne place,
les Blancs correspondent a une bonne couleur mais celle-ci est mal placée
Bon courage !!''').pack(padx =15, pady =10)
def menu(fenetre):     #Création de la barre de menu avec ses boutons
    "Barre de menu"
    top=Menu(fenetre)
    fenetre.config(menu=top)
    J=Menu(top)
    top.add_cascade(label='Jeu',menu=J,underline=0)#création de la cascade Jeu
    J.add_command(label='Nouvelle partie',command=jouer,underline=0)#création du bouton Nouvelle partie
    J.add_command(label='Essai',command=nouvelessai,underline=0)#etc
    J.add_command(label='Montrer la combinaison',command=victoire,underline=0)
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
                finalList[i] = choice(idColorList)        # tirage au sort d'une couleur dans la liste: colorList[]
                # Tracé d'un rectangle et des cercles représentant la combinaison à rechercher
                plateau.create_oval ((i+1)*40-15, 10, (i+1)*40+15, 40, outline = "black")
                txt = plateau.create_text((i+1)*40, 25, text="?", font="Arial 16 ", fill="blue")
def victoire():
        """ Pour révéler la suite recherchée... """ 
        for i in range (len(finalList)):
                plateau.create_oval ((i+1)*40-15, 10, (i+1)*40+15, 40, fill = colorList[finalList[i]])
        plateau.create_text(400, 255, text="La partie est terminée !", font="Arial 16 ", fill="blue")
        global jouant
        jouant = False
def color(event):
    if jouant:
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
                        currentList[i] = nbClic     #permet la coloration des cercles
        nbClic = nbClic+1        
def jouer():
        """ Gestion du jeu: le clic sur le bouton "essai", déclenche l'évaluation de la combinaison proposée"""
        # Mise en place du bouton "essai N°":
        """ C'est à partir de l'ACTION sur ce bouton qu'il faut continuer le MOTEUR DU JEU """
        plateau.delete(ALL)     #supprime tout sur le plateau pour reinitialiser le plateau
        global num
        num = 1
        creerCercle(num)        # appelle la mise en place des cercles qui seront colorés par: color(event)
        tirage()
        global jouant
        jouant = True
def nouvelessai():
    print("Nouvel essai. Jouer :")
    print(jouant)
    if jouant == True:
        global num
        num = num+1
        if num > 10:
            victoire()
        
        creerCercle(num)
        for i in range(4):
            plateau.create_oval ((i+6)*40-15, 35+(num - 1)*35-15, (i+6)*40+15, 35+(num - 1)*35+15, outline = "white")
        
        i = 0
        confirme = 0
        colorCount = [0, 0, 0, 0, 0, 0]
        for j in range(4):
            colorCount[finalList[j]] = colorCount[finalList[j]] + 1
        for j in range(4):
            colorCount[currentList[j]] = colorCount[currentList[j]] - 1
            if finalList.count(currentList[j]) >= 1 and colorCount[currentList[j]] >= 0:
                plateau.create_oval ((i+6)*40-15, 35+(num - 1)*35-15, (i+6)*40+15, 35+(num - 1)*35+15, fill = "white")
                if currentList[j] == finalList[j]:
                    plateau.create_oval ((i+6)*40-15, 35+(num - 1)*35-15, (i+6)*40+15, 35+(num - 1)*35+15, fill = "red")
                    confirme = confirme + 1

                i = i + 1
                    
        if confirme == 4:
            victoire()
    
                
def creerCercle(num):      #mise en place des cercles colorés
        """ Mise en place des cercles de la proposition, avant leur coloration"""
        for i in range (4):
                # mise en place cercles
                cercle = plateau.create_oval ((i+1)*40-15, 35+num*35-15, (i+1)*40+15, 35+num*35+15, outline = "white")
                cercleCoord.insert (i, plateau.coords (cercle))        # Récupère les coordonnées des cercles
def quitter():       #créé la fenêtre  pour quitter la partie
        reponse=askokcancel('KingMind',"Tu veux vraiment quitter ? On fait pas la belle ?") 
        if reponse:
                fenetre.destroy() 
##### PROGRAMME PRINCIPAL #####
        
fenetre= Tk()
fenetre.title('KingMind 0.2')
plateau = Canvas(fenetre, height =700,width=400, bg='black' )
plateau.pack(side =RIGHT, padx =0, pady =0)
essaiBouton = Button(fenetre, text = ("Essai"), command =nouvelessai)        
essaiBouton.pack(side=TOP, padx=0, pady=20)
menu(fenetre)
#bkg = PhotoImage(file='bkg.gif')
#imageboite()
# La méthode bind() permet de lier un événement avec une fonction
plateau.bind('<Button-1>',color)
fenetre.mainloop()
