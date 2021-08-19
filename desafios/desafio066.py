soma = contador = 0
while True:
    n = int(input('Digite um número, 999 para finalizar: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} e a soma é {soma}')
