# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:32:01 2020

@author: Mane González
"""

"""
	estrategi 1:
	preguntar todo y sumar los puntajes finalizar colocando los puntajes 
	y tomando la determinacion si es ave,reptil,o mamifero
"""
import json

clasificacion = [0,0,0]
tipo = ""
c = 0
mayor = 0
indice = 0
z = 0

with open('animales.json') as file:
	data = json.load(file)

for pregunta in data['Nodo']:
	print('TIENE')
	print(pregunta[1])
	R = input("")
	if R == "S":
		clasificacion[0] = clasificacion[0] + int(pregunta[2]["Ave"])
		clasificacion[1] = clasificacion[1] + int(pregunta[2]["Reptil"])
		clasificacion[2] = clasificacion[2] + int(pregunta[2]["Mamifero"])

for cont in clasificacion:
	if clasificacion[z] > mayor:
		mayor = clasificacion[z]
		indice = z
	z = z +1
z = 0

if indice == 0:
	print("AVE")
if indice == 1:
	print("REPTIL")
if indice == 2:
	print("MAMIFERO")

