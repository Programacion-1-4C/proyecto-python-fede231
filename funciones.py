import random
from random import randint
palabras_wordle = {1.:'fabula',
                   2.:'fallos',
                   3.:'define',
                   4.:'franca',
                   5.:'salmon',
                   6.:'chayle',
                   7.:'emboca',
                   8.:'filial',
                   9.:'grabas',
                   10.:'flores',
                   11.:'radios',
                   12.:'santos',
                   13.:'turcos',
                   14.:'verdes',
                   15.:'salvay',
                   16.:'partir',
                   17.:'cabeza',
                   18.:'calvos',
                   19.:'ciegos',
                   20.:'edades',
                   21.:'eolica',
                   22.:'teclas',
                   23.:'estuve',
                   24.:'cantar',
                   25.:'iconos',
                   26.:'brazos',
                   27.:'pierna',
                   28.:'pastas',
                   29.:'querer',
                   30.:'esnifa',
                   31.:'enviar',
                   32.:'gallos',
                   33.:'horcas',
                   34.:'jubilo',
                   35.:'latido',
                   36.:'libros',
                   37.:'suerte',
                   38.:'perdon',
                   39.:'pensar',
                   43.:'monton',
                   44.:'minion',
                   45.:'moscas',
                   46.:'tiempo',
                   47.:'mentir',
                   48.:'negros',
                   49.:'niggas',
                   50.:'polipo',
                   51.:'leches',
                   52.:'lirios',
                   53.:'madres',
                   54.:'ingles',
                   55.:'herido',
                   56.:'italia',
                   57.:'mostro',
                   58.:'boludo',
                   59.:'lacras',
                   60.:'lamina',
                   61.:'lapida',
                   62.:'mantos',
                   63.:'lentes',
                   64.:'llaves',
                   65.:'nalgas',
                   66.:'naipes',
                   67.:'ositos',
                   68.:'oxidar',
                   69.:'muerta',
                   70.:'oculta',
                   71.:'pactos',
                   72.:'palmas',
                   73.:'palito',
                   74.:'palpas',
                   75.:'ordeno',
                   76.:'muelas',
                   77.:'perros',
                   78.:'persas',
                   79.:'picara',
                   80.:'quesos',
                   81.:'quiero',
                   82.:'reales',
                   83.:'remojo',
                   84.:'robots',
                   85.:'ruanda',
                   86.:'saltos',
                   87.:'sensor',
                   88.:'siento',
                   89.:'trucos',
                   90.:'tubitos',
                   91.:'traigo',
                   92.:'trajes',
                   93.:'tarifas',
                   94.:'techos',
                   95.:'bombas',
                   96.:'judios',
                   97.:'vibras',
                   98.:'agudos',
                   99.:'angulo',
                   100.:'lionel',
                   101.:'messis',
                   102.:'apodos',
                   103.:'barcos',
                   104.:'bardos'
                   }

colores = {
    'verde': '\033[92m',
    'amarillo': '\033[93m',
    'rojo': '\033[91m',
    'ENDC': '\033[0m',
}
def color_de_letra(letra, color):
    return colores[color] + letra + colores['ENDC']





