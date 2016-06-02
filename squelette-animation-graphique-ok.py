# -*- coding: cp1252 -*-
#  
#  LOUIS PAYEN 2014
# Squelette de programme pour faire rapidement
# et facilement des animations graphiques simples
# L'objectif est de se concentrer sur l'algorithme !

from scipy import *
from Tkinter import *
import Tkinter
import os
import time
from msvcrt import kbhit,getch
import winsound
import threading


class MyTimer:
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
        
    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()


def affiche_tableau(x1,y1):
	os.system("cls")
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print

		
def tableau_graphique(xmax,ymax):
	r=9   # facteur d'échelle
	for x in range(xmax):
		for y in range(ymax):
			if t[y,x] == 1:
				#can.create_rectangle(x*20, y*20, x*20+18, y*20+18, fill='blue')
				try:
					pave1 = can.create_image(x*20, y*20, image=image_pave1, anchor=NW)
				except Exception, e:
					bidon=1
				
				
			if t[y,x] == 2 or t[y,x] == 0:
				try:
					can.create_rectangle(x*20, y*20, x*20+2*r, y*20+2*r, fill='black')
				except Exception, e:
					bidon=1	
				
			if t[y,x] == 3:   #  Souris
				try:
					can.create_oval(x*20, y*20, x*20+2*r, y*20+2*r, fill='yellow')
				except Exception, e:
					bidon=1
								
			if t[y,x] == 8:
				try:
					can.create_rectangle(x*20, y*20, x*20+18, y*20+18, fill='red')
				except Exception, e:
					bidon=1				
				
			if t[y,x] == 6:
				try:
					can.create_oval(x*20, y*20, x*20+18, y*20+18, fill='blue')
				except Exception, e:
					bidon=1					
					
					
def initialiser():
	can.delete(ALL)			
	tableau_graphique(15,12)
	
def lance_timer():
	global timehb,flagtimer
	if flagtimer==0:
		flagtimer=1
		timehb.start()    #Lance le timer 1 seule fois !
		
	
# Routine executée par le timer cycliquement :
def gestion(unstr):
	global compteur_hb
	
	compteur_hb = compteur_hb+1
	
	if compteur_hb == 25:
		can.delete(ALL)			# efface les objets en mémoire
		compteur_hb =0				# sans quoi cela sature


	# Appeler ici toutes les routines que vous devez exécuter cycliquement :
	animation()     










	# Raffraichissement des tableaux (uniquement ici !) :

	tableau_graphique(15,12)
	
	affiche_tableau(15,12)





# Exemple de routine pour déplacement auto :	
def animation():
	global x1,sens1
	t[9,x1]=0
	x1 = x1+sens1
	t[9,x1]=3
	if x1>10 or x1<2:
		sens1 = -sens1
	

# Routine de gestion du clavier 
# A modifier en fonction de ce que vous voulez faire

def clavier(evt):
	global xp
	

	if (evt.char=='4') and (xp>1) :
		t[11,xp]=0
		xp=xp-1
		t[11,xp]=3
		
	if (evt.char=='6') and (xp<13) :
		t[11,xp]=0
		xp=xp+1
		t[11,xp]=3


# Rajouter toutes vos routines ici :
















#-----------------------------------------		
	
# INITIALISATION du programme principal :
# Initialisez toutes les variables globales et tableau ici :
						
t=zeros([12,15],int) # t[y,x] y= et x=10
y=9
x=2
a=2
xp=4
sens=1
compteur_hb = 0
x1=4
sens1=1
flagtimer=0

t[0,] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
t[1,] = [1,8,8,8,8,8,8,8,8,8,8,8,8,8,1]
t[2,] = [1,8,8,8,8,8,8,8,8,8,8,8,8,8,1]
t[3,] = [1,8,8,8,8,8,8,8,8,8,8,8,8,8,1]
t[4,] = [1,8,8,8,8,8,8,8,8,8,8,8,8,8,1]
t[5,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[6,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[7,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[8,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[9,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[10,] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
t[11,] = [1,2,2,2,3,2,2,2,2,2,2,2,2,2,1]



fin_boucle=0
i_boucle=0
reset1=0
# Création du timer pour la gestion routines cycliques :
timehb = MyTimer(0.3, gestion, ["MyTimer"])

# Création de la fenetre graphique :
fen = Tk()
image_pave1 = PhotoImage(file='mur.gif')
can = Canvas(fen, width =500, height =400, bg ='black')
can.pack(side =TOP, padx =100, pady =100)


b1 = Button(fen, text =' Initialiser ', command =initialiser)
b1.pack(side =LEFT, padx =3, pady =3)

b2 = Button(fen, text ='lancer timer', command =lance_timer)
b2.pack(side =LEFT, padx =30, pady =3)

b3 = Button(fen, text =' Quitter ', command =fen.quit)
b3.pack(side =LEFT, padx =80, pady =3)


texte=Tkinter.Text(fen, width=70, height=5)
texte.insert(Tkinter.END,'Touche 4 et 6 pour déplacement ')
texte.pack(side=Tkinter.LEFT)

winsound.PlaySound("boum1.wav", winsound.SND_ASYNC)

# impératif pour que tout fonctionne :
fen.bind_all('<Key>', clavier)

fen.mainloop()
fen.destroy()
	
timehb.stop()           # Arret du timer

