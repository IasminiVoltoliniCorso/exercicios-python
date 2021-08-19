v = float(input('Qual é a velocidade do carro?'))
if v > 80:
    print('Você foi MULTADO! Excedeu o limite de velocidade da via de 80 km/h.')
    m = (v - 80) * 7
    print('Você recebeu uma multa de R$ {:.2f} reais.'.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança.')
