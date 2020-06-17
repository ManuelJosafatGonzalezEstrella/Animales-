# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:14:28 2020

@author: Mane González
"""

import json
with open('busqueda.json') as file:
	data = json.load(file)
camino=[]

def busqueda(cuspide,valorbusqueda):
	
	if cuspide == valorbusqueda:
		return valorbusqueda
		
	for v in data:
		if v[0] == cuspide:
			camino.append(cuspide)
			print(v[0])
			resultado=busqueda(v[1],valorbusqueda)
			if resultado:
				return resultado
	camino.pop()
	
resultado=busqueda("C:","CallOfDuty.exe")
if resultado:
	print ("Se encontro el archivo")
	print(camino)
else:
	print("no hay no existe")
