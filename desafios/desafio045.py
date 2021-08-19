from random import randint
from time import sleep
itens = ('Pedra', 'Tesoura', 'Papel')
print('''Suas opções:
 [0] PEDRA
 [1] TESOURA
 [2] PAPEL''')
n = int(input('Qual sua jogada?'))
if 0 <= n <= 2:
    c = randint(0, 2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ...')
    sleep(1)
    print('{:-^40}'.format(''))
    print('Computador jogou {}'.format(itens[c]))
    print('Jogador jogou {}'.format(itens[n]))
    print('{:-^40}'.format(''))
    if c == 0:
        if n == 0:
            print('\033[1;36m EMPATE!\033[m')
        elif n == 1:
            print('\033[1;31m VOCÊ PERDEU!\033[m')
        elif n == 2:
            print('\033[1;32m VOCÊ VENCEU!\033[m')
    elif c == 1:
        if n == 0:
            print('\033[1;32m VOCÊ VENCEU!\033[m')
        elif n == 1:
            print('\033[1;36m EMPATE!\033[m')
        elif n == 2:
            print('\033[1;31m VOCÊ PERDEU!\033[m')
    elif c == 2:
        if n == 0:
            print('\033[1;31m VOCÊ PERDEU!\033[m')
        elif n == 1:
            print('\033[1;32m VOCÊ VENCEU!\033[m')
        elif n == 2:
            print('\033[1;36m EMPATE!\033[m')
else:
    print('\033[1;33m OPÇÃO INVALIDA!\033[m')
