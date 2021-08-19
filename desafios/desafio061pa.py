print('\033[1;34mProgressão Aritmétrica [PA]\033[m')
a1 = int(input('Digite um valor para ser o 1º termo da PA: '))
r = int(input('Digite um valor para ser a RAZÂO da PA: '))
print('A sequência da PA será:')
n = a1
c = 1
while c <= 10:
    print('{}.'.format(n), end=' ')
    n += r
    c += 1
print('FIM.')
