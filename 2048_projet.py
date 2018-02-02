# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:31:46 2018

@author: 3404503
"""

import numpy as np, random
import sys

class Grille :
    """Classe deffinissant une grille de jeu"""
    
    def __init__(self):
        """la grille initiale est un tableau 4x4 de zero avec deux boîtes"""
        self.plateau = [0]*16
        i = random.choice(range(16))
        j = i
        while i==j:
            j=random.choice(range(16))
        self.plateau[i] = self.plateau[j] = 2
        self.plateau = np.reshape(self.plateau,(4,4))
        return 
       
    def memoire(self,n, dico):
        """Garde les anciens coup en memoire"""
        m = [0]*16
        m = np.reshape(m,(4,4))
        for i in range(4):
            for j in range(4):
                m[i,j] = self.plateau[i,j] 
        dico[n] = m
        n = n+1 
        return n, dico
    
    def pop(self) :
        """Cette méthode crée une nouvelle case de valeur aléatoire entre 2 et 4 à une position aléatoire sur le plateau"""
        a = np.random.randint(1,3)
        valeur = 2*a
        x = np.random.randint(0,4)
        y = np.random.randint(0,4)
        while self.plateau[x,y] != 0:            
            x = np.random.randint(0,4) 
            y = np.random.randint(0,4)
        self.plateau[x,y] = valeur
        print(self.plateau)
    
    def collision_up(self):
        for j in range(4):
            if self.plateau[0,j] == self.plateau[1,j]:
                self.plateau[0,j] = self.plateau[0,j]*2
                self.plateau[1,j] = 0
                self.up()
            elif self.plateau[1,j] == self.plateau[2,j]:
                self.plateau[1,j] = self.plateau[1,j]*2
                self.plateau[2,j] = 0
                self.up()
            elif self.plateau[2,j] == self.plateau[3,j]:
                self.plateau[2,j] = self.plateau[2,j]*2
                self.plateau[3,j] = 0
                self.up()    

    def collision_down(self):
        self.plateau = self.plateau[[3,2,1,0],:]
        self.collision_up()
        self.plateau = self.plateau[[3,2,1,0],:]
            
    def collision_right(self):
        self.plateau = np.transpose(self.plateau)
        self.collision_down()
        self.plateau = np.transpose(self.plateau)
    
    def collision_left(self):
        self.plateau = np.transpose(self.plateau)
        self.collision_up()
        self.plateau = np.transpose(self.plateau)
                    
    
    
    def up(self):
       """Deplacement de une case vers le haut"""
       for i in [1,2,3]:
           for j in range(4):
               if self.plateau[i,j] != 0:
                   if self.plateau[i-1,j] == 0:
                       self.plateau[i-1,j] = self.plateau[i,j]
                       self.plateau[i,j] = 0
                        
                   
    def left(self):
        self.plateau = np.transpose(self.plateau)
        self.up()
        self.plateau = np.transpose(self.plateau)
    
    def  down(self) :
        self.plateau = self.plateau[[3,2,1,0],:]
        self.up()
        self.plateau = self.plateau[[3,2,1,0],:]
    
    def right(self) :
        self.plateau = np.transpose(self.plateau)
        self.down()
        self.plateau = np.transpose(self.plateau)
    
        
    
    def mouve(self):
        ok = False         
        m = input('Your mouve ? Choose 1 quit, 0 new game: ')
        m = int(m)
        if m == 8:
            for i in range(4):
                self.up()
                ok = True
            self.collision_up()
        elif m == 5:
            for i in range(4):
                self.down()
                ok = True
            self.collision_down()
        elif m == 4:
            for i in range(4):
                self.left()
                ok = True
            self.collision_left()
        elif m == 6:
            for i in range(4):
                self.right()
                ok = True
            self.collision_right()
        elif m == 0 :
            print('Recommençons!')
            newgame()
            ok = True
        elif m == 1:
            sys.exit("Salut.")

        return ok

    def check(self, tours, histoire):
            n = 0
            memoire = histoire[tours-1]
            for i in range(4):
                for j in range(4):
                    if self.plateau[i,j] == 2048:
                        print("Vous avez gagné")
                        return 2
                    if self.plateau[i,j] != 0 :
                        n = n + 1
                        if n == 16:
                            self.collision_up()
                            self.collision_left()
                            if np.array_equiv(self.plateau, memoire) == True:
                                print("Perdu")
                                return 2
                            else :
                                self.plateau = memoire
                                return 0
                    else:
                        return 0    
                            

def newgame():
    tours = 0
    histoire = {}
    grille = Grille()
    print(grille.plateau)
    a = 0
    while a == 0:
        ok = grille.mouve()
        while ok != True : 
            ok = grille.mouve()
        
        grille.pop()
        tours, histoire = grille.memoire(tours, histoire)
        a = grille.check(tours, histoire)
    
     
def continu():     
    m = input('Continue ? (y or n):')
    ok = False
    if m == 'y' :
         ok = True
         newgame()
    if m == 'n':
        ok = True
        sys.exit("Salut.")
    return ok
        

if __name__=='__main__':
    print("launched as main script!")
    
    newgame()
    oki = False
    while oki != True:
        ok = continu()