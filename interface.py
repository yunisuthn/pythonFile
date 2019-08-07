# -*- coding: Latin-1 -*- 
#from Tkinter import * 
# coding: utf-8
from tkinter import * 
from math import *
 
 
#Fonction calcul 
def calcul (): 
    #Récupération des variables
    D=int(A.get()) 
    E=int(B.get()) 
    F=int(C.get()) 
 
    #Calcul 
    delta=(E*E)-(4*D*F)
    chaine3.configure(text = delta)
    #G=D+E+F
    if delta <0:
        #print ("Pas de solutions") # Lorsque delta est négatif, il n'y a pas de solutions
        chaine.configure(text = "Pas de solutions")
    if delta ==0:
        chaine.configure(text = "Une solution")
        #print ("Une solution") # Lorsque delta est égale à 0, il y a une solution X
        x=-int(E)/2*int(D) # Calcul de X
        chaine1.configure(text = "X= {}".format(x))
        #print ("X=",x) # On affiche la solution   
    if delta >0:
        chaine.configure(text = "Deux solutions")
        racine_carre_delta=sqrt(delta)
        k=-E-racine_carre_delta
        l=-E+racine_carre_delta
        m=2*D 
        x1=int(k)/int(m) # Calcul de X1
        x2=int(l)/int(m) # Calcul de X2
        chaine0.configure(text = "X1= {}".format(x1))
        chaine1.configure(text = "X2= {}".format(x2))
            
 
fenetre = Tk() 
fenetre.title("Test de calculs") 
 

txt=Label(fenetre, text="Programme qui calcule les racines d'un polynome du second degré .").grid(row=1, column=2) 
txt0=Label(fenetre, text="Tel que Ax²+Bx+C=0").grid(row=2, column=2) 
txt1=Label(fenetre, text="A:").grid(row=3, column=1) 
txt2=Label(fenetre, text='B:').grid(row=4, column=1) 
txt3=Label(fenetre, text='C:').grid(row=5, column=1)
Button(fenetre,text='Calculer',command=calcul).grid(row=6 , column=1) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=6, column=2) 
 
A=Entry(fenetre) 
B=Entry(fenetre) 
C=Entry(fenetre)
chaine = Label(fenetre) 
chaine0 = Label(fenetre) 
chaine1 = Label(fenetre)  
chaine3 = Label(fenetre)
 
A.grid(row=3, column=2) 
B.grid(row=4, column=2) 
C.grid(row=5, column=2)
chaine.grid(row=7, column=2)  
chaine3.grid(row=7, column=1) 
chaine0.grid(row=8, column=1)
chaine1.grid(row=8, column=2)  
 
fenetre.mainloop()

 
#from tkinter import * 

#fenetre = Tk()

#label = Label(fenetre, text="Hello World")
#label.pack()

# bouton de sortie
# bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
# bouton.pack()



# # txt = Text(fenetre, height=5, width=20, wrap=WORD)
# txt.insert('1.0', 'Saisir du texte sans couper les mots...')
# txt.pack(side=TOP)
#Button(fenetre, text='fetch', command=fetch).pack()

# fenetre.mainloop()

