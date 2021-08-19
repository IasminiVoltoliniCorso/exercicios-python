d = float(input('Qual é a distância da sua viagem?'))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('O valor da sua passagem será de R$ {:.2f} reais.'.format(p))