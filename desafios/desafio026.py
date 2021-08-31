f = str(input('Digite uma frase:')).strip().lower()
print('A letra "a" aparece {} vezes.'.format(f.count('a')))
print('A primeira vez que a letra "a" aparece é na posição {}.'.format(f.find('a') + 1))
print('A última vez que a letra "a" aparace é na posição {}.'.format(f.rfind('a') + 1))
print('Quantidade de carateres total: {} '.format(len(f)))



