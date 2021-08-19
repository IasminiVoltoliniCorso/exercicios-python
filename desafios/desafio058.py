from random import randint
cont = 1
c = randint(0, 10)
print('\033[1;34m=='*19)
print('''Sou seu computador...
Tente adivinhar o número que estou pensando entre 0 e 10.''')
print('\033[1;34m==\033[m'*19)
j = int(input('Qual é o seu palpite?  '))
while not j == c:
    cont += 1
    if c < j:
        j = int(input('\033[36mMENOS... Tente novamente.\033[m'))
    else:
        j = int(input('\033[35mMAIS... Tente novamente.\033[m'))
print('\033[1;34mPARABÉNS! Você acertou com {} tentativas.\033[m'.format(cont))
