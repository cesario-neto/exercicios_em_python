"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

combustivel = input('Que combustível você vai querer? G = gasolina (R$2,50), A = álcool (R$1,90): ')
combustivel = combustivel.lower()
combustivel = combustivel.strip()

if combustivel == 'g' or combustivel == 'gasolina' or combustivel == 'ga' or combustivel == 'gc':
    litros = int(input('Quantos litros vai querer abastecer: '))
    if litros >= 1 and litros <= 20:
        desconto = (4/100) * 2.50
        valor_total = (litros * 2.50) - (desconto * litros)
        
        print(f'O cliente irá pagar R${valor_total:.2f} para {litros}l de combustivel')
        print(f'Valor cheio R${(litros * 2.50):.2f}')
        print(f'Desconto de 4%, (-R${(desconto * litros):.2f})')
        
    elif litros > 20:
        desconto = (6/100) * 2.50
        valor_total = (litros * 2.50) - (desconto * litros)
        
        print(f'\nO cliente irá pagar R${valor_total:.2f} para {litros}l de combustivel')
        print(f'Valor cheio R${(litros * 2.50):.2f}')
        print(f'Desconto de 6%, (-R${(desconto * litros):.2f})')
        
    
elif combustivel == 'a' or combustivel == 'alcool' or combustivel == 'álcool' or combustivel == 'etanol' or combustivel == 'et' or combustivel == 'ec' or combustivel == 'e':
    litros = int(input('Quantos litros vai querer abastecer: ')) # desconto é de 3% abaixo de 20l e 5% acima de 20l e o valor do produto é de R$1,90
    if litros >= 1 and litros <= 20:
        desconto = (3/100) * 1.90
        valor_total = (litros * 1.90) - (desconto * litros)
        
        print(f'\nO cliente irá pagar R${valor_total:.2f} para {litros}l de combustivel')
        print(f'Valor cheio R${(litros * 1.90):.2f}')
        print(f'Desconto de 3% (- R${(desconto * litros):.2f})')
        
    elif litros > 20:
        desconto = (5/100) * 1.90
        valor_total = (litros * 1.90) - (desconto * litros)
        
        print(f'\nO cliente irá pagar R${valor_total:.2f} para {litros}l de combustivel')
        print(f'Valor cheio R${(litros * 1.90):.2f}')
        print(f'Desconto de 5% (- R${(desconto * litros):.2f})')
    
else:
    print('Combustivel invalido')