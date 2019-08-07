from math import * # Permet d'importer la fonction racine carré "sqrt(nombre)"
recommencer=0 # Permet de redémarer le programme lorsqu'il est fini
while recommencer!=1:
    print ("Programme qui calcule les racines d'un polynome du second degré .")
    print ("Tel que Ax²+Bx+C=0")
    A=input('A=') # On rentre la valeur de A
    B=input('B=') # On rentre la valeur de B
    C=input('C=') # On rentre la valeur de C
    delta=(int(B)*int(B))-(4*int(A)*int(C)) # On calcule delta, le discriminant, en fonction de A,B et C
    print ("Delta=",delta) # On affiche la valeur de delta
    if delta <0:
        print ("Pas de solutions") # Lorsque delta est négatif, il n'y a pas de solutions
    if delta ==0:
        print ("Une solution") # Lorsque delta est égale à 0, il y a une solution X
        x=-int(B)/2*int(A) # Calcul de X
        print ("X=",x) # On affiche la solution   
    if delta >0:
        print ("Deux solutions") # Lorsque delta est positif,il y a deux solutions, X1 et X2
        racine_carre_delta=sqrt(delta) # On calcul la racine carré de delta
        k=-int(B)-racine_carre_delta # Variable qui va intervenir dans le calcul de X1
        l=-int(B)+racine_carre_delta # Variable qui va intervenir dans le calcul de x2
        m=2*A # Variable qui va intervenir dans le calcul de X1 et X2
        x1=int(k)/int(m) # Calcul de X1
        x2=int(l)/int(m) # Calcul de X2
        print ("X1=",x1) # On affiche la première solution
        print ("X2=",x2) # on affiche la deuxième solution
    print ("Fin du programme!")
    print ("Voulez-vous recommencer ?")
    recommencer=input('0. Oui\n1. Non\n')