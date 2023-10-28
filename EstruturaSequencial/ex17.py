"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
from math import ceil

tamanho = int(input('Digite o tamanho em m²: '))
litros = tamanho / 3
# latas
latas = ceil(litros / 18)
# galoes
galoes = ceil(litros / 3.6)
# mistura latas e galoes
mistura_latas = int(litros / 18)
mistura_galoes = int((litros - (mistura_latas * 18)) / 3.6)

if litros - (mistura_latas * 18) % 3.6 != 0:
    mistura_galoes += 1

print(f'Em {tamanho}m², você precisará de {litros:.2f}l. Você pode comprar {latas} lata de tinta que custará no total R${latas * 80:.2f}')
print(f'Em {tamanho}m², você precisará de {litros:.2f}l. Você pode comprar {galoes} galões de tinta que custará no total R${galoes * 25:.2f}')
print(f'Em {tamanho}m², você precisará de de forma mais econômica {mistura_latas} latas e {mistura_galoes} galões de tinta que custará no total R${((mistura_latas * 80) + (mistura_galoes * 25)):.2f}')



