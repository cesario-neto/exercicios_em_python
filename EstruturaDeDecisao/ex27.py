"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morango = input('Quantos Kg de morango você vai querer levar? ')
morango = morango.replace(',', '.')

maca = input('Quantos Kg de maçã você vai querer levar? ')
maca = maca.replace(',', '.')

peso = float(morango) + float(maca)


if peso > 0 and peso <= 5:
    preco_morango = float(morango) * 2.50
    preco_maca = float(maca) * 1.80
    preco_total = preco_morango + preco_maca
    
if peso > 5:
    preco_morango = float(morango) * 2.20
    preco_maca = float(maca) * 1.50
    
    preco_total = preco_morango + preco_maca
    
    if preco_total > 25 or peso >= 8:
        preco_total = preco_total - (preco_total * 10/100)

print(f'Você vai levar {morango}kg de morango e {maca}kg de maçã.')
print(f'No total vai custar R${preco_total:.2f}')