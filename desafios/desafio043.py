p = float(input('Qual é o seu peso?'))
a = float(input('Qual é a sua altura?'))
imc = p / (a**2)
print('O seu IMC é de {:.2f} kg/m², '.format(imc),end='')
if imc < 18.5:
    print('você está {}ABAIXO{} do peso.'.format('\033[1;31m', '\033[m'))
elif 18.5 <= imc < 25:
    print('{}PARABÉNS...{} Você está com o peso ideal.'.format('\033[1;35m', '\033[m'))
elif 25 <= imc < 30:
    print('você está com {}SOBREPESO{}.'.format('\033[1;33m', '\033[m'))
elif 30 <= imc < 40:
    print('{}Sinto muito!{} Você tem obsidade.'.format('\033[1;31m', '\033[m'))
else:
    print('{}Sinto muito!{} Você tem obsidade mórbida.'.format('\033[1;31m', '\033[m'))


