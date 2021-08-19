n = int(input('Diga um número:'))
#print('A tabuada deste número é:\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}\n{}x{}={}'.format(n, 1, n*1,n, 2, n*2,n, 3, n*3,n, 4, n*4,n, 5, n*5,n, 6, n*6,n, 7, n*7,n, 8, n*8,n, 9, n*9,n, 10, n*10))
print('A tabuada deste número é:')
print('-'*13)
for cont in range(1, 11):
       print('{} x {:2} = {:2}'.format(n, cont, n * cont))
print('-'*13)
