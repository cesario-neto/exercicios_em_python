"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
from math import ceil

tamanho = int(input('Digite o tamanho em m²: '))
litros = tamanho / 3
latas = ceil(litros / 18)

print(f'Em {tamanho}m², você precisará de {litros:.2f}l. Você terá de comprar {latas} lata de tinta que custará no total R${latas * 80:.2f}')








