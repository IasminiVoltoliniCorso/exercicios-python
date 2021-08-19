print('\033[2;35m==\033[m'*12)
print('          CADASTRO DE PESSOAS')
print('\033[2;35m==\033[m'*12)
total18 = totalM = totalF = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Genero: [M / F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalM += 1
    elif idade < 20:
        totalF += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja contunuar? [S / N]:  ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Total de homens cadastrados: {totalM}')
print(f'Total de mulheres com menos de 20 anos: {totalF}')