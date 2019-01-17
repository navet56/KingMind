#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *      
from random import *
from tkinter.messagebox import  askokcancel

# Variables :

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple','white','grey','pink']        # Liste des couleurs disponibles
idColorList = [0, 1, 2, 3, 4, 5, 6, 7, 8]										  # Liste qui assigne des chiffres aux couleurs
finalList = [0,0,0,0]                                                  # Liste de la combinaison de couleurs à deviner, généré par l'ordinateur
currentList = [0, 0, 0, 0]                                                # Liste des couleurs choisies par le joueur
cercleCoord = []                                                          # Liste, de listes  = coordonnées des 4 cercles, d'un essai   
nbClic = 0                                                                # gestion du nombre de "clic gauche souris", utilisée pour sélectionner une couleur
nbreEssai = 1
jouant = False

#Fonctions d'interfaces et de graphismes :

def aPropos():         #Création de la section "à propos"             
    msg =Toplevel() 
    Message(msg, width=200, aspect=200, justify=CENTER, 
        text ='''KingMind
Par Evan Diberder, Mael Le Boulicaut, Kilian Buan
Tk version 8.4
Python 3.7
Version 1.2''').pack(padx =15, pady =10)

def imageboite():
    plateau.create_image(200, 350, image=bkg)
def imageking():
	plateau.create_image(150, 600, image=theking)

def presentation():    #Création de la section "présentation"
    msg =Toplevel() 
    Message(msg, width =200, aspect =150, justify =CENTER, 
        text ='''----Presentation du jeu----
Le but du jeu est de trouver la combinaison magique choisie par l'ordinateur.
Sélectionne parmis 6 couleurs puis l'ordinateur te dira, grâce a des ronds rouges ou blancs la proximité avec la bonne combinaison.''').pack(padx =15, pady =10)

def deroule():         #Création de la section "déroule"
    msg =Toplevel() 
    Message(msg, width =200, aspect =100, justify =CENTER, 
        text ='''----Comment jouer à KingMind----
Pour changer les couleurs, il faut cliquer sur les 4 cercles qui vous sont présentés.
Pour voir si votre combinaison est la bonne, il faut cliquer sur le bouton essai à gauche.
A chaque essai, 4 points de couleur rouges ou blancs vous sont présentés :
Les Rouges correspondent à une bonne couleur à la bonne place,
les Blancs correspondent a une bonne couleur mais celle-ci est mal placée
Bon courage !!''').pack(padx =15, pady =10)
def menu(fenetre):     #Création de la barre de menu avec ses boutons
    "Barre de menu"
    top=Menu(fenetre)#on nome le menu "top"
    fenetre.config(menu=top)#on configure la fenetre pour que le menu de cette fenetre soit "top"
    J=Menu(top)#J est un sous-menu de top
    top.add_cascade(label='Jeu',menu=J,underline=0)#création de la cascade Jeu
    J.add_command(label='Nouvelle partie',command=jouer,underline=0)#création du bouton Nouvelle partie
    J.add_command(label='Essai',command=nouvelessai,underline=0)#etc
    J.add_command(label='Abandonner (montrer la reponse)',command=findujeu,underline=0)
    R=Menu(top)#R est un sous-menu de top
    top.add_cascade(label='Regles',menu=R,underline=0)
    R.add_command(label='Présentation',command=presentation,underline=0)
    R.add_command(label='Déroulé',command=deroule,underline=0)
    O=Menu(top)#etc
    top.add_cascade(label='Options',menu=O,underline=0)
    O.add_command(label='A propos',command=aPropos,underline=0)
    O.add_command(label='Quitter le jeu',command=quitter,underline=0)

#Coeur des fonctions du programme principal :

def tirage():
        """ Tirage de la combinaison de couleur à deviner + Mise en forme: suite de 5 couleurs à deviner """
        # Tracé d'un rectangle et des cercles représentant la combinaison à rechercher
        idColorList = [0, 1, 2, 3, 4, 5, 6, 7, 8]										  # Liste qui assigne des chiffres aux couleurs
        plateau.create_rectangle(10, 58, 190, 92, outline='white',fill='black') #création du rectangle autour de des 4 ronds de la combinaison finale
        for i in range (4):
                finalList[i] = choice(idColorList)        # tirage au sort d'une couleur dans la liste: idColorList
                txt = plateau.create_text((i+1)*40, 76, text="?", font="Arial 16 ", fill="white")
                idColorList.remove(finalList[i])
def color(event):
    if jouant:
        """ Gestion de l'événement "Clic gauche", sur un cercle, pour sélectionner une couleur """
    
        global nbClic
        if nbClic >= 8: nbClic = 0
        # position du pointeur de la souris:
        X = event.x
        Y = event.y
        # Identification du cercle "cliqué" + sélection d'une couleur
        for i in range (4):
                if (cercleCoord [i][0] <= X <= cercleCoord [i][2]) and (cercleCoord [i][1] <= Y <= cercleCoord [i][3]):
                        plateau.create_oval (cercleCoord[i], fill = colorList[nbClic])
                        currentList[i] = nbClic     #permet la coloration des cercles en fonction du clic
        nbClic = nbClic+1        
def jouer():
        """ Gestion du jeu: le clic sur le bouton "essai", déclenche l'évaluation de la combinaison proposée"""
        # Mise en place du bouton "essai N°":
        """ C'est à partir de l'ACTION sur ce bouton qu'il faut continuer le MOTEUR DU JEU """
        plateau.delete(ALL)     #supprime tout sur le plateau pour reinitialiser le plateau et supprimer l'image de la boite notamment
        global nbreEssai
        nbreEssai = 1					#cette variable va nous servir pour créer les 4 cercles
        creerCercle(nbreEssai)        # appelle la mise en place des cercles qui seront colorés par: color(event)
        tirage()				#on éffectue le choix aléatoire et on place les points d'interrogations
        global jouant
        jouant = True			#jouant est un booleen permettant entre autre de bloquer le bouton essai si nouvelle partie n'est pas actif, la on le met actif car nouvelle partie est actionné
        plateau.create_text(90, 32, text="Combinaison", font="Arial 14 ", fill="white") #on créé le texte pour indiquer à quoi sert cette colonne, ici :la colonne pour entrer les combinaisons
        plateau.create_text(290, 32, text="Indice", font="Arial 14 ", fill="white") #on créé le texte pour indiquer à quoi sert cette colonne, ici ; la colonne qui donne les indices

def nouvelessai():              #fonction du bouton Essai, qui créer 4 cercles en dessous de ceux d'avant et compare avec la cominaison magique
    if jouant == True:
        global nbreEssai
        nbreEssai = nbreEssai+1
        if nbreEssai > 10:
            findujeu()
        creerCercle(nbreEssai)
        indice()
def indice():
    """Fonction permettant d'afficher les indices"""
    confirme = 0 #initialisation de confirme
    j = 0 #permet de pas avoir les ronds d'indice à la même place que les ronds de la 
    for i in range(4):
        if currentList[i] in finalList:#si une couleur de la liste actuelle est dans la lkste finale
            if currentList[i] == finalList[i] :#et si la couleur est egal à celle dans la liste finale à la meme pas (d'ou le [i])
                plateau.create_oval ((j+6)*40-15, (nbreEssai-1)*35+70, (j+6)*40+15, (nbreEssai - 1)*35+100, fill = "red")#on place une boule rouge
                confirme = confirme + 1#on incrémente confirme de 1
                j = j + 1
            if currentList[i] in finalList and currentList[i] != finalList[i]:#si une couleur de la liste actuelle est dans la lkste finale mais pasbonne place
                plateau.create_oval ((j+6)*40-15, (nbreEssai-1)*35+70, (j+6)*40+15, (nbreEssai - 1)*35+100, fill = "white")#on place une boule blanche
                j = j + 1
        if confirme == 4:#si confirme est de 4, c'est que les 4 couleurs sont égals
            findujeu()#on lance la fonction de fin du jeu, de victoire"
def findujeu():
    """ Pour révéler la suite recherchée... """ 
    global jouant
    if jouant == True:
        for i in range (len(finalList)):
            plateau.create_oval ((i+1)*40-15, 60, (i+1)*40+15, 90, fill = colorList[finalList[i]]) #on affiche la combinaison finale
        jouant = False #on désactive jouant pour ne plus que les actions marchent
        imageking() #on affiche l'image de fin
        plateau.create_text(150, 720, text="La partie est terminée.", font="Arial 16 ", fill="white") #on créé le texte qui dit fin de partie
def creerCercle(nbreEssai):      #mise en place des cercles colorés
        """ Mise en place des cercles de la proposition, avant leur coloration"""
        for i in range (4):# mise en place des cerlces
                cercle = plateau.create_oval ((i+1)*40-15, nbreEssai*35+70, (i+1)*40+15, nbreEssai*35+100, outline = "white")
                cercleCoord.insert (i, plateau.coords (cercle))        # Récupère les coordonnées des cercles
def quitter():       #créé la fenêtre  pour quitter la partie
        reponse=askokcancel('KingMind',"Tu veux vraiment quitter ? On fait pas la belle ?") #on utilise la fonction askokcancel de la bibliothèque messagebox de tkinter
        if reponse:#si reponse (c'est a dire askokcancel) est active (donc qu'on a cliqué sur ok)
                fenetre.destroy() #fermer la fenetre (la "detruire")
                exit()
# Lancement du programme :
        
fenetre= Tk()#bibliothèque tkinter permet de faire des fenetres graphiques
fenetre.title('KingMind 1.2')# titre de la fenetre
plateau = Canvas(fenetre, height =750,width=400, bg='black' )
plateau.pack(side =RIGHT, padx =0, pady =0)
can=Canvas(fenetre,height=750,width=200, bg='black') #espace de gauche utilisé pour le bouton essai
can.pack(side=LEFT) 
selObject=can
essaiBouton = Button(can, text = ("Essai"), command =nouvelessai)        
essaiBouton.pack(side=TOP, padx=0, pady=364) 
menu(fenetre)
bkg = PhotoImage(file='bkg.gif')
theking = PhotoImage(file='theking.gif')
imageboite()#la fenetre du jeu demarre directement sur l'image de la boite du jeu officiel
# La méthode bind() permet de lier un événement avec une fonction
plateau.bind('<Button-1>',color)
fenetre.mainloop()
