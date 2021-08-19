nome = str(input('Qual é o seu nome completo? ')).upper().strip()
print('Nome: {}'.format(nome.title()))
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))









