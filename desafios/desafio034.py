s = float(input('Qual é o salário do funcionário? R$ '))
if s <= 1250.00:
    a = s * 0.15  # 'a' aumento
else:
    a = s * 0.10
print('Quem ganhava R$ {:.2f} reais, passa a ganhar R$ {:.2f} reais.'.format(s, (s + a)))


