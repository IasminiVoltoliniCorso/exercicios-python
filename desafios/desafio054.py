from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    idade = int(input('Qual é o ano de nascimento da {}ª pessoa: '.format(c)))
    al = date.today().year
    ano = al - idade
    if ano >= 21:
        ma += 1
    else:
        me += 1
print('''A quantidade de pessoas MAIORES de idade é de: {};
A quantidade de pessoas MENORES de idade é de: {}'''.format(ma, me))

