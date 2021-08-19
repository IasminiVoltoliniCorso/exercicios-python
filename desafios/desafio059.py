from time import sleep
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
o = 0
while o != 5:
    print('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números 
        [ 5 ] Sair do programa''')
    o = int(input('Qual é a sua opção?'))
    if o == 1:
        s = n1 + n2
        print('\033[1;36mA soma de {} com {} é {}\033[m'.format(n1, n2, s))
    elif o == 2:
        m = n1 * n2
        print('\033[1;35mA multiplicação de {} com {} é {}\033[m'.format(n1, n2, m))
    elif o == 3:
        if n1 > n2:
            print('\033[1;34mO maior é {}\033[m '.format(n1))
        elif n2 > n1:
            print('\033[1;33mO maior é {}\033[m '.format(n2))
        else:
            print('\033[1;32mEles são iguais.\033[m')
    elif o == 4:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif o == 5:
        print('\033[1;31mFinalizando...\033[m')
    else:
        print('Opção inválida. Tente novamente.')
    print('\033[1;34m-*-\033[m'*15)
    sleep(3)
print('Volte sempre.')
