print('\033[2;36m~~~\033[m'*10)
print('{:^65}'.format('\033[3;35mBANCO 24 HORAS \033[m'))
print('\033[2;36m~~~\033[m'*10)
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 200
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R$ {cedula} reais.')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('\033[2;36m~~~\033[m'*10)
print('\033[3;35m VOLTE SEMPRE! TENHA UM BOM DIA!\033[m')
print('\033[2;36m~~~\033[m'*10)