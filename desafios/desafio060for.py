f = 1
n = int(input('Digite um número para calcular o fatorial: '))
for c in range(n, 0, -1):
    print('{}'.format(c),end=' ')
    print(' x ' if c > 1 else ' = ',end=' ')
    f *= c
print('{}'.format(f))
