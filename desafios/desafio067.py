while True:
    print('\033[1;34m*=*\033[m' * 13)
    tab = int(input('Qual tabuada você quer ver:  '))
    print('\033[1;34m*=*\033[m' * 13)
    if tab < 0:
        break
    for cont in range (1,11):
        print(f'{tab} X {cont} = {tab*cont}')
print('\033[1;34mPrograma tabuada encerrado. Volte sempre!\033[m')

