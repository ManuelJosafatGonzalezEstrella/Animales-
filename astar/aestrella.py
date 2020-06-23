# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:55:38 2020

@author: Mane González
"""

tablero = [[1],[1],[0],[0],[1],[3],
           [0],[0],[0],[0],[1],[0],
           [0],[2],[0],[0],[0],[0],
           [0],[0],[0],[0],[0],[0],
           [0],[0],[0],[0],[0],[0],
           [0],[0],[0],[0],[0],[0]]
valores = []
caminorecorrido = []

def astar(inicio,fin,tablero):
    tt = 0
    rr = 0
    for t in range(len(tablero)):
        for r in range(len(tablero[t])):
            if((t==13)and(r==0)):
                print(tablero[t][r])
    
astar([1,2],[0,5],tablero)
