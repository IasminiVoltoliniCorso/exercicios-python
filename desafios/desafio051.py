print('\033[1;35mProgressão Aritmétrica ''PA''\033[m')
a1 = int(input('Digite um valor para ser o 1º termo da PA: '))
r = int(input('Digite um valor para ser a RAZÂO da PA: '))
print('A sequência da PA será:')
for c in range(1, 11):
    c = a1 + (c - 1) * r
    print('{}.'.format(c),end=' ')
print('FIM.')
