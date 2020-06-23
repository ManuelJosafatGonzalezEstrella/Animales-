# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:38:10 2020

@author: Mane González
"""

import json
import random
from operator import itemgetter

with open('subcolina.json') as file:
	data = json.load(file)

NodosRuta=[]

NodoSig=[]

Hijos=[]

neXt = []
def subidadelacolina(inicio,final,nodoAnterior):
    NodosRuta.append(inicio)
    print("======================================")
    print("Inicial "+inicio)
    print("Anterior "+nodoAnterior)
    if neXt:
        del neXt[:]
        del Hijos[:]
    if final == inicio:
        print("Si fue encontrado")
        return inicio
    if nodoAnterior == "":
        nodoAnterior = inicio

    for d in data:
        if d[0] == inicio:
            if nodoAnterior != "":
                if d[1] != nodoAnterior:
                    Hijos.append(d)
    

  
    print(min(Hijos, key=itemgetter(2))[:])
    
    menores = (min(Hijos, key=itemgetter(2))[2])

   
    for c in Hijos:
        if c[2] == menores:
           
            neXt.append(c)
    print("Estos son los caminos posibles")
    print(neXt)
    numMenores = 0
    for n in neXt:
        numMenores = numMenores +1
       
        if numMenores > 1:
            r = random.random()
  
            if r < 0.5:
                neXt.pop()
            else: 
                neXt.pop(0)
        else:
            print("")
    if neXt:
        for n in neXt:
            print("Camino elegido")
            print(n[1])
            return subidadelacolina(n[1],final,inicio)
    print("--------------------------------------------")

def hijos(lista,actual):
    H = filter(lambda  a: a[0] == actual,lista)
    return list(H)   
arch=subidadelacolina("Z","I","")
if arch:
    print("Nodo encontrado")
    print(arch)
    print("Ruta recorrida")
    print(NodosRuta)