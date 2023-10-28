"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota_bimestre = input('Digite as 4 nota do aluno separando-o por ",": ')
nota_bimestre = nota_bimestre.split(',')

media_das_notas = [int(v) for v in nota_bimestre ]
print(f'A média do aluno é {sum(media_das_notas) / len(media_das_notas)}')
