"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
# A área do quadrado é calculada multiplicando a medida do comprimento pela medida da largura.

area_quadrado = input('Digite o comprimento de um lado do quadrado: ')
area_quadrado = int(area_quadrado)
print(f'A área do quadrado é {(area_quadrado * area_quadrado)} e o dobro é {(area_quadrado * area_quadrado) * 2}')