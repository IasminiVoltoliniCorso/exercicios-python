dias = int(input('Qual o periodo do alugual do veículo?'))
km = float(input('Quantos Km foram rodados?'))
p1 = dias * 60  #(p) = preço
p2 = km * 0.15
total = p1 + p2
print('O valor total à pagar será de R$ {:.2f}.'.format(total))

