from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
al = date.today().year  # ano atual
idade = al - ano
print('A sua idade é {} anos.'.format(idade))
if idade < 18:
    print('Você ainda não tem idade para se alistar no exercito. Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Esse ano você precisa se apresentar no exercito.')
elif idade > 18:
    print('Já se passou {} anos desde o prazo para se apresentar no exercito.'.format(idade - 18))
    a = str(input('Você se apresentou no exercito?')).lower().strip()
    if a == 'sim':
        print('Ótimo, você está em dia com serviço militar.')
    elif a == 'não' or 'nao':
        print('Você perdeu o prazo. Pode ter que pagar uma multa ou ser preso.')
    else:
        print('Resposta invalida, apenas resposta "sim ou não".')
