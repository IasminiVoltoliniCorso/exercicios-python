print('---'*17)
print('Vamos analizar se três retas formam um triÂngulo.')
print('---'*17)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Esses três segmentos formam um triângulo.')
else:
    print('Esses segmentos NÃO formam um triângulo.')