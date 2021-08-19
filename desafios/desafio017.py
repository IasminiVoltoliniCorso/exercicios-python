import math
a = float(input('Diga um número: ')) #cateto adjacente
b = float(input('Diga outro número: ')) #cateto oposto
h = math.sqrt((a**2) + (b**2))
#math.hypot(a, b) formula da hipotenusa
print('Sabendo que o {} é o cateto adjacente'.format(a))
print('E o {} é o cateto oposto'.format(b))
print('A hipotenusa deste triângulo retângulo é {:.2f}'.format(h))
