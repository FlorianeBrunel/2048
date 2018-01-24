# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:23:00 2018

@author: Brunel
"""
 

 


import numpy as np

class Grille :
    """Classe deffinissant une grille de jeu"""
    
    def __init__(self):
        """la grille initiale est un tableau 4x4 de zero (absance de boite)"""
        self.plateau = np.zeros(16).reshape(4,4)
    
    

    
    
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
        
    def up(self):
       """Deplacement de une case vers le haut"""
       for i in [1,2,3]:
           for j in range(4):
               if self.plateau[i,j] != 0:
                   if self.plateau[i-1,j] == 0:
                       self.plateau[i-1,j] = self.plateau[i,j]
                       self.plateau[i,j] = 0
                   if self.plateau[i-1,j] == self.plateau[i,j]:
                       self.plateau[i-1,j] = self.plateau[i,j]*2
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
        m = ''
        m = input('Your mouve ? (U (Up), D (Down), L (Left), R (Right)): ')
        
        if m == 'U':
            for i in range(4):
                self.up()
        elif m == 'D':
            for i in range(4):
                self.down()
        elif m == 'L':
            for i in range(4):
                self.left()
        elif m == 'R':
            for i in range(4):
                self.right()
        """rajoute une case sur le plateau"""
        self.pop()


    def check(self):
            n = 0
            for i in range(4):
                for j in range(4):
                    if self.plateau[i,j] == 2048:
                        print("Vous avez gagné")
                        return 1
                    if self.plateau[i,j] != 0 and self.plateau[i-1,j]!= self.plateau[i,j] and self.plateau[i+1,j] != self.plateau[i,j] and self.plateau[i,j-1] != self.plateau[i,j] and self.plateau[i,j+1] != self.plateau[i,j] :
                        n = n + 1
                        if n == 16:
                            print("Perdu")
                            return 2
                    else:
                        return 0    
                            
                    
       
if __name__=='__main__':
    print("launched as main script!")
    
    a = 0
    
    grille = Grille()
    grille.pop()
    
    while a == 0:
        grille.mouve()   
        a = grille.check()
   
