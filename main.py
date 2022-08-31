from funciones import *
win = False
palabra_random = random.choice(palabras_wordle)

print('Escribi tu palabra\n>>>')
tabla = []
for i in range(6):
    tabla.append(['_' for l in range(6)])

vidas = 0
while (not win) and (vidas < len(palabra_random)):
    palabra = input('')
    while len(palabra) != len(palabra_random):
        print(f'la palabra debe tener {len(palabra_random)} letras')
        palabra = input('')

    if palabra_random == palabra:
        print('ganaste paaaaa')
        tabla[vidas]= [l for l in palabra]
        win = True
    else:
        colorsito = []
        for j in range(len(palabra)):
            if palabra[j] == palabra_random[j]:
                colorsito.append(palabra[j])
            elif palabra[j] in palabra_random:
                colorsito.append(color_de_letra(palabra[j], 'amarillo'))

            else:
                colorsito.append(color_de_letra(palabra[j], 'rojo'))
        tabla[vidas] = colorsito
    for i in range(6):
        print(" ".join(tabla[i]))

    vidas += 1
if win:
    print(f'ganaste paaa, la palabra era {palabra_random}')
else:
    print(f'perdiste salame la palabra era {palabra_random}')
