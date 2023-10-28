"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""
# C = 5 * ((F-32) / 9).

temp = int(input('Digite a temperatura em Fahrenheit: '))

print(f'{temp}°F convertido em celsius fica {5 * ((temp-32) / 9):.2f}°C')