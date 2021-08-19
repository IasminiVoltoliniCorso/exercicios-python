a = float(input('Qual é a altura da parede em metros?'))
l = float(input('Qual é a largura da parede em metros?'))
area = a * l
print('A área desta parede é {:.2f} m²'.format(area))
print('Você irá precisar de {:.2f} litros de tinta para tinta essa parede.'.format(area/2))



