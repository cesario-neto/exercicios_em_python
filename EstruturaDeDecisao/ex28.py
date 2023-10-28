"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
tipo_carne = input('Você vai querer File Duplo, Alcatra ou Picanha? ')
tipo_carne = tipo_carne.lower()

if tipo_carne == 'file duplo' or tipo_carne == 'alcatra' or tipo_carne == 'picanha':
    if tipo_carne == 'file duplo':
        quantidade = input('Quantos kg você vai querer? ')
        quantidade = quantidade.replace(',', '.')
        tipo_carne = tipo_carne.title()
        
        if float(quantidade) > 0 and float(quantidade) <= 5:
            preco = float(quantidade) * 4.90
        elif float(quantidade) > 5:
            preco = float(quantidade) * 5.80
            
    if tipo_carne == 'alcatra':
        quantidade = input('Quantos kg você vai querer? ')
        quantidade = quantidade.replace(',', '.')
        tipo_carne = tipo_carne.title()
        
        if float(quantidade) > 0 and float(quantidade) <= 5:
            preco = float(quantidade) * 5.90
        elif float(quantidade) > 5:
            preco = float(quantidade) * 6.80
            
    if tipo_carne == 'picanha':
        quantidade = input('Quantos kg você vai querer? ')
        quantidade = quantidade.replace(',', '.')
        tipo_carne = tipo_carne.title()
        
        if float(quantidade) > 0 and float(quantidade) <= 5:
            preco = float(quantidade) * 6.90
        elif float(quantidade) > 5:
            preco = float(quantidade) * 7.80
           
    forma_pagamento = input('Qual vai ser a forma de pagamento? Dinheiro em especie(1), cartão débito(2), cartão crédito(3), cartão Tabajara(4): ')
    if forma_pagamento == '1' or forma_pagamento == '2' or forma_pagamento == '3' or forma_pagamento == '4':
        if forma_pagamento == '1':
            forma_pagamento = 'Dinheiro'
            desconto = 0.00
        if forma_pagamento == '2':
            forma_pagamento = 'Cartão débito'
            desconto = 0.00
        if forma_pagamento == '3':
            forma_pagamento = 'Cartão crédito'
            desconto = 0.00
        if forma_pagamento == '4':
            forma_pagamento = 'Cartão Tabajara'
            desconto = (preco * 5/100)
        print()
        print('=============NOTA FÍSCAL=======================')
        print(f'Produto.......................{tipo_carne}')
        print(f'Quantidade....................{float(quantidade):.2f}kg')
        print(f'Metódo de pagamento...........{forma_pagamento}')
        print(f'Preço total...................R${preco:.2f}')
        print(f'Desconto......................R${desconto:.2f}')
        print(f'Total a pagar.................R${(preco - desconto):.2f}')
        print('===============================================')
        
        
    else:
        print('Digite apenas o número referente a forma de pagamento.')
            
            
else:
    print('Só temos essas três opções de carne')