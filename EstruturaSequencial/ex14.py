"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input('Quanto quilos você touxe dessa vez? '))
excesso = 50
multa = 4.00

if peso > excesso:
    peso_multa = peso - excesso
    peso_multa = int(peso_multa)
    print(f'Você excedeu o peso limite de {excesso}Kg trazendo {peso}Kg, você terá que pagar R${peso_multa * multa:.2f} à mais de multa')
else:
    print(f'O peso limite é de 50Kg e você trouxe {peso:.3f}Kg, não excedendo o peso limite então não terá que pagar uma multa. ')