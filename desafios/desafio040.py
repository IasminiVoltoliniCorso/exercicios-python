n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2)/2
print('Com as notas {:.1f} e {:.1f} sua média é {:.1f}'.format(n1, n2, m))
if m < 5:
    print('Você foi {}REPROVADO.{}'.format('\033[1;31m','\033[m'))
elif m >= 5 and m <= 6.9:
    print('Você ficou em {}RECUPERAÇÃO.{}'.format('\033[1;33m', '\033[m'))
else:
    print('PARABÉNS. Você foi {}APROVADO.{}'.format('\033[1;32m', '\033[m'))
