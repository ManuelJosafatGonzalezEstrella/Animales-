# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 00:08:16 2020

@author: Mane González
"""



"""Este tablero se modifica"""
tablero =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
"""Guardando todas las posiciones actuales"""
posAct=[]
llave = 0
"""numero de Intentos """
posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def reinas(nreinas, tablero, llave,posiciones):
    backup = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("nreinas "+str(nreinas))
    """Si se cumple el numero de reinas indicado se dirije a la solucion"""
    if nreinas == 1:
        return solucion(tablero)
    else: 
        for t in range(len(tablero)):
            for r in range(len(tablero[t])):
                """Contador para llenar solo una reina por iteración recursiva"""
                if cont == 0:
                    """El estado 3 es donde ya paso por esa posicion
                    """
                    """verifica que la posicion para colocar a la reina no haya sido usada
                    anteriormente o si no es un camino """
                    """"la matriz de visitados se llena con 3 si ya se visito"""
                    if posiciones[t][r] != 3:
                        if(tablero[t][r] == 0):
                            """Si no hay reinas colodadas se coloca, el visitado y la reina en
                            el tablero, se bloquea con cont"""
                            if nreinas == 4:
                                posiciones[t][r] = 3
                            tablero[t][r] = 1
                            cont = cont + 1
                            """se almacena una posicion temporal 
                            para enviarla a el llenado de sus movimientos"""
                            posAct.append([t,r])
        """Se guarda el nuevo tablero con los movimientos de la reina actual
        posAct"""
        tablero = vertHorz(tablero,posAct)
        """Eliminacion de la posicion actual"""
        posAct.pop(0)
        for t in tablero:

            if 0 in t:
                """si aun existe un espacion sin ser camino o una reina se sigue con 
                la recursividad"""
                llave = 0
            else:
                """Si ya no hay un lugar para nuevas reinas se resetea la matriz"""
                llave = 1
        if llave == 1:
            print(llave)
            for t in backup:
                print(t)
            nreinas=4
            llave=0
            return reinas(nreinas,backup,llave,posiciones)
        if llave == 0:
            print(llave)
            nreinas=nreinas-1
            return reinas(nreinas,tablero,llave,posiciones)
"""====================Agrega las diagonales verticales y horizontales====================="""
def vertHorz(tablero,posAct):
    print("=============================================")
    a = posAct[0][0]
    b = posAct[0][1]
    r = range(len(tablero))
    bb = b
    aa = a
    print(posAct)
    
    for t in range(len(tablero)):
        for r in range(len(tablero[t])):
            tablero[a][r] = 2
            tablero[t][b] = 2
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb-1
        aa = aa -1
        if (bb >= 0)and(aa >=0):
            print("- -")
            tablero[aa][bb] = 2
    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        aa = aa +1
        bb = bb +1
        if (aa <= r)and(bb <= r):
            print("+ +")
            tablero[aa][bb] = 2

    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb+1
        aa = aa -1
        if (bb < r)and(aa >=0):
            print("+ -")
            tablero[aa][bb] = 2
    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb-1
        aa = aa + 1
        if (bb >= 0)and(aa <r):
            print("- +")
            tablero[aa][bb] = 2
    tablero[a][b]=1
    imp(tablero)
    print("=============================================")
    return tablero
    
"""Se agrega la ultima reina en caso de que haya una """
def solucion(tablero):
    for t in range(len(tablero)):
        for r in range(len(tablero[t])):
            if (tablero[t][r]) == 0:
                tablero[t][r] = 1
    print("===Solucion===")
    for t in tablero:
        print(t)

def imp(tablero):
    print("--------------------")
    for t in tablero:
        print(t)

reinas(4,tablero,0,posiciones)

