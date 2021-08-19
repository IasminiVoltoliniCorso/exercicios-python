print('~~'*20)
print('\033[1;34m                     SEQUÊNCIA DE FIBONACCI\033[m')
print('~~'*20)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[35m~~\033[m'*20)
print('{} ¬ {}'.format(t1, t2), end=' ')
c = 3
while c <= n:
    t3 = t1 + t2
    print('¬ {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    c += 1
print('Fim.')
print('\033[35m~~\033[m'*20)