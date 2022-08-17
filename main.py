import random
from funciones import palabras_wordle
from funciones import elegir_palabra
from funciones import letras_repetidas
from funciones import letras_no_usadas
from funciones import contar_letras
from funciones import acertar_palabra


print('que vas a hacer?')
intentos = 0
while True:
    decision = input('1. Jugar'
                     '2. Agregar palabras'
                     '3.salir')
    if decision == '1':
        elegir_palabra(palabras_wordle)
        intento = input('dame una letra')
        intento = intentos+1
        if intentos > 5:
            break

    elif decision == '2':
        palabra = input('que palabra vas a agregar')
        palabras_wordle.append(palabra)


    elif decision == '3':

    else:
        break