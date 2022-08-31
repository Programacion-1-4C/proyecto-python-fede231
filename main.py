import random
from funciones import *
win = False
palabra_random = random.choice(palabras_wordle)

decision = input('1. Jugar\n')
if decision == '1':
    print('escribi tu palabra')
    board = []
    for i in range(6):
        board.append(['_' for l in range(6)])

    game_loop_counter = 0
    while (not win) and (game_loop_counter < len(palabra_random)):
        text = input ('')
        while len (text) != len(palabra_random):
            print(f'la palabra debe tener {len(palabra_random)} letras')
            text = input('')


        if palabra_random == text:
            print('ganaste paaaaa')
            board[game_loop_counter] = [l for l in text]
            win = True
        else:
            test_line = []
            for j in range(len(text)):
                if text[j] == palabra_random[j]:
                    test_line.append(text[j])
                elif text[j] in palabra_random:
                    test_line.append(color_letter(text[j],'yellow'))

                else:
                    test_line.append(color_letter(text[j],'red'))
            board[game_loop_counter] = test_line
        for i in range(6):
            print(" ".join(board[i]))

        game_loop_counter += 1
    if win:
        print(f'ganaste paaa, la palabra era{palabra_random}')
    else:
        print(f'perdiste salame la palabra era{palabra_random}')





