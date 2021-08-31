print('---'*11)
print('Vamos analizar o triângulo.')
print('---'*11)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Ótimo, temos um triângulo. ',end='')
    if a == b == c:
        print('Sendo classificado como triângulo EQUILÁTERO.')
    elif a == b != c or b == c != a or a == c != b:
        print('Sendo classificado como triângulo ISÓSCELES.')
    elif a != b != c != a:
        print('Sendo classificado como ESCALENO.')
else:
    print('Esses valores NÃO foram um triângulo.')
    print('Tente novamente.')

