from random import randint
from time import sleep
c = randint(0, 5) # computador
print('***-' * 13)
print('Vou pensar um número entre 0 e 5. Tente adivinhar...')
print('***-' * 13)
n = int(input('Em qual número eu pensei?')) # jogador
print('PROCESSANDO...')
sleep(3)
if n == c:
    print('Parabéns! Você acertou.')
else:
    print('Sinto muito! Você errou. Eu pensei no {} e não no {}.'.format(c, n))
