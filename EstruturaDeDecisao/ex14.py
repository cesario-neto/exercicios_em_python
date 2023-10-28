"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1 = input('Digite a primeira nota do aluno: ')
nota2 = input('Digite a segunda nota do aluno: ')

try:
    lista = []
    lista.append(nota2)
    lista.append(nota1)
    media_nota = ((int(nota1) + int(nota2)) / int(len(lista)))
    
    if int(nota1) < 0 or int(nota1) > 10 or int(nota2) < 0 or int(nota2) > 10:
        
        print('A nota do aluno deve ser entre 0 e 10')
        
    else:
        if media_nota > 0 and media_nota <= 4.0:
            conceito = 'E'
        if media_nota > 4.0 and media_nota <= 6.0:
            conceito = 'D'
        if media_nota > 6.0 and media_nota <= 7.5:
            conceito = 'C'
        if media_nota > 7.5 and media_nota <= 9.0:
            conceito = 'B'
        if media_nota > 9.0 and media_nota <= 10:
            conceito = 'A'
        
        print(f'Primeira nota: {int(nota1)}')
        print(f'Segunda nota: {int(nota2)}')
        print(f'A média do aluno foi: {media_nota}')
        print(f'O aluno tirou um {conceito}')
        
        if conceito == 'E' or conceito == 'D':
            print('Está Reprovado')
        elif conceito == 'C' or conceito == 'B' or conceito == 'A':
            print('Está aprovado')
    
except ValueError:
    print('Digite apenas números')