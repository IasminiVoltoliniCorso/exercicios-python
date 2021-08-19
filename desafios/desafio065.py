resp = 'S'
cont = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números  a médias entre eles é {}'.format(cont, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
