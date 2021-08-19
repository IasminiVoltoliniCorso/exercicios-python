somaidade = 0
media = 0
velho = 0 # maior idade de homem
nomevelho = ' '
novas = 0
for p in range(1, 5):
    print('\033[1;35m-----{}ª Pessoa-----\033[m'.format(p))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Genero: [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        novas += 1
media = somaidade / 4
print('A média das idades é de: {} anos'.format(media))
print('O nome do homem mais velho é {}, ele tem {} anos.'.format(nomevelho, velho))
print('No grupo tem {} mulheres com menos de 20 anos.'.format(novas))
