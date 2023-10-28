"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
soma_nota = nota + nota2

if soma_nota / 2 >= 10:
    print('Nossa... Aprovado com Distinção!')
elif soma_nota / 2 >= 7:
    print('Parabéns! Você passou.')
elif soma_nota / 2 < 7:
    print('Poxa... Você reprovou.')