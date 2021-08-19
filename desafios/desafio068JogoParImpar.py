from random import randint
venceu = 0
print('\033[3;35m==\033[m' * 11)
print('\033[1;36mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[3;35m==\033[m' * 11)
while True:
    comp = randint(0, 10)
    opcao = ' '
    while opcao not in 'PI':
        opcao = (input('PAR OU ÍMPAR? [P / I]: ')).strip().upper()[0]
    n = int(input('Diga um número: '))
    soma = n + comp
    print(f'Você jogou {n} e o computador {comp}. Total de {soma}',end=' ')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('\033[1;36m VOCÊ GANHOU!\033[m')
            venceu += 1
        else:
            print('\033[1;31m VOCÊ PERDEU!\033[m')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print('\033[1;36m VOCÊ GANHOU!\033[m')
            venceu += 1
        else:
            print('\033[1;31m VOCÊ PERDEU!\033[m')
            break
    print("Let's play again...")
print(f"GAME OVER! Você ganhou {venceu} vezes")
