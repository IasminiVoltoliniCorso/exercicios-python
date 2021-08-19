print('\033[1;34mProgressão Aritmétrica [PA]\033[m')
a1 = int(input('Digite um valor para ser o 1º termo da PA: '))
r = int(input('Digite um valor para ser a RAZÂO da PA: '))
print('A sequência da PA será:')
n = a1
c = 1
t = 0
mais = 10
while mais != 0:
    t += mais
    while c <= t:
        print('{}.'.format(n), end=' ')
        n += r
        c += 1
    print('Pausa.')
    mais = int(input('\033[1;34mQuantos termos você quer monstrar mais?\033[m'))
print('Ao total foram {} termos apresentados.'.format(t))
print('FIM.')
