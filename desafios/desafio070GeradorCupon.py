print('\033[2;35m***\033[m'*10)
print('         \033[1;34mSUPER BARATÃO\033[m')
print('\033[2;35m***\033[m'*10)
soma = valorMil = cont = barato = 0
nameBarato = ' '
while True:
    name = str(input('Nome do produto: ')).strip().upper()
    price = float(input('Preço: R$ '))
    cont += 1
    soma += price
    opcao = ' '
    if price > 1000:
        valorMil += 1
    if cont == 1 or price < barato:
        barato = price
        nameBarato = name
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S / N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total da compra: R$ {soma:.2f}')
print(f'Temos {valorMil} produtos custando mais de R$ 1.000,00 reais.')
print(f'O produto mais barato é {nameBarato}, custando R$ {barato:.2f} reais.')
