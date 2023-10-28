"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
valor_produtos = input('Digite o valor dos produtos separando por , :')
valor_produtos = valor_produtos.split(',')
lista_com_valor = [float(valor_produto) for valor_produto in valor_produtos]
lista_com_valor = sorted(lista_com_valor)
print(f'O produto mais barato custa: {lista_com_valor[0]:.2f}')