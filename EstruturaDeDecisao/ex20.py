"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota = input('digite a nota do aluno separando com vírgula (obs: se a nota for com números decimais, coloque um ponto para indicar tais números): ')
lista = nota.split(',')

if len(lista) > 3:
    print('Digite apenas 3 notas do aluno')
elif len(lista) < 3:
    print('Digite as 3 notas do aluno')
    
else:
    lista_notas = []
    for num in lista:
        lista_notas.append(float(num))
    
    if lista_notas[0] < 0 or lista_notas[0] > 10 or lista_notas[1] < 0 or lista_notas[1] > 10 or lista_notas[2] < 0 or lista_notas[2] > 10:
        print('A nota do aluno deve ser entre 0 e 10')
        
    else:
        media = 0

        for num in lista:
            media += float(num)
        
        media = media / len(lista)
        
        if media == 10:
            print(f'Sua média foi de {media:.1f}, parabéns! Você foi aprovado com distição')
        elif media >= 7:
            print(f'Sua média foi de {media:.1f}, parabéns! Você foi aprovado')
        elif media < 7:
            print(f'Sua média foi de {media:.1f}, Você Reprovou')