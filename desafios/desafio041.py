from datetime import date
ano = int(input('Informe o ano de nascimento:'))
al = date.today().year # ano atualmente
id = al - ano # idade
print('A idade do atleta é de {} anos.'.format(id))
if id <= 9:
    print('Classificação: {}MIRIM{}'.format('\033[1;35m', '\033[m'))
elif id <= 14:
    print('Classificação: {}INFANTIL{}'.format('\033[1;35m', '\033[m'))
elif id <= 19:
    print('Classificação: {}JUNIOR{}'.format('\033[1;35m', '\033[m'))
elif id <= 20:
    print('Classificação: {}SENIOR{}'.format('\033[1;35m', '\033[m'))
else:
    print('Classificação: {}MASTER{}'.format('\033[1;35m', '\033[m'))
