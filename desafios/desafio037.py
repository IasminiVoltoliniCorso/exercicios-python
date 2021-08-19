n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[1] Conserter para BINÁRIO;
[2] Converter para OCTAL;
[3] Converter para HEXADECIMAL.''')
o = int(input('Qual é a sua opção?'))
if o == 1:
    print('{} convertendo para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertendo para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertendo para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida.')



