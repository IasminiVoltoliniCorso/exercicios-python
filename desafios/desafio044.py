print('{:*^40}'.format(' LOJA RENNER '))
p = float(input('Qual é o valor do produto? R$ '))
print('''Escolha a opção de pagamento:
[1] À vista: dinheiro ou cheque;
[2] À vista no cartão;
[3] Em até 2x no cartão;
[4] 3x ou mais no cartão.''')
c = float(input('Qual é a condição de pagamento?'))
if c == 1:
     print('Com 10% de desconto, o valor a pagar será de R$ {:.2f} reais.'.format(p - (p * 0.1)))
elif c == 2:
     print('Com 5% de desconto, o valor a pagar será de R$ {:.2f} reais.'.format(p - (p * 0.05)))
elif c == 3:
    print('O valor da paracela será de R$ {:.2f} reais.'.format(p/2))
elif c == 4:
    q = int(input('Quantas parcelas?'))
    j = p + (p * 0.2) # juros
    par = j / q
    print('Parcelendo em {}x, o valor da parcela será de R$ {:.2f} reais, tendo juros de 20%, o valor total a pagar será de R$ {:.2f} reais.'.format(q, par, j))
else:
    print('{}Opção invalida!{}'.format('\033[1;31m', '\033[m'))
