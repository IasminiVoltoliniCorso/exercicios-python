num = cont = soma = 0
num = int(input('Digite um número [digite 999 para encerrar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [digite 999 para encerrar]: '))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
print('Acabou!')
