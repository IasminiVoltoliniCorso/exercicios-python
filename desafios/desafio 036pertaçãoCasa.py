c = float(input('Qual é o valor da casa? R$ ')) # casa
s = float(input('Qual é o seu salário? R$ ')) # salário
t = int(input('Quantos anos de financiamento? ')) # tempo
m = t * 12 # convertendo para meses
p = c / m # parcela
v = s * 0.3 # condição: não pode ultrassar 30% do salario
print('Para pagar uma casa de R$ {:.2f} reias em {} anos, a pertação será de R$ {:.2f} reais.'.format(c, t, p))
if p >= v:
    print('Seu emprestimo pode ser {}NEGADO.{}'.format('\033[1;31m','\033[m'))
else:
    print('Seu emprestimo  pode ser {}APROVADO.{}'.format('\033[1;32m','\033[m'))

