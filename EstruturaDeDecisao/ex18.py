"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

1. Se o dia é entre 1 e 31.
2. Se o mês é entre 1 e 12.
3. Ano esta no intervalo entre 1900 e 2100
4. Se mês for 04, 06, 09 ou 11, dia pode ser no máximo 30;
5. Se mês for 02, dia pode ser no máximo 28;
6. Se ano for bissexto e mês for 02, dia pode ser no máximo 29.
"""

try:
    data = input('Digite uma data aqui separando dia, mes e ano com /: ')
    lista = data.split('/')
    lista_inteiros = []
    for num in lista:
        lista_inteiros.append(int(num))
    
    valido = True
    
    if (lista_inteiros[2]%4) == 0:
        if (lista_inteiros[2]%100) == 0:
            if (lista_inteiros[2]%400) == 0:
                bissexto = True
            else:
                bissexto = False
        else:
            bissexto = True
    else:
        bissexto = False
        
    
    if lista_inteiros[0] >= 1 and lista_inteiros[0] <= 31:
        if lista_inteiros[1] >= 1 and lista_inteiros[1] <= 12:
            if lista_inteiros[2] < 1900 or lista_inteiros[2] > 2100:
                valido = False
                
            if lista_inteiros[1] == 4 or lista_inteiros[1] == 6 or lista_inteiros[1] == 9 or lista_inteiros[1] == 11:
                if lista_inteiros[0] < 1 or lista_inteiros[0] > 30:
                    valido = False
            
            if lista_inteiros[1] == 2:
                if bissexto == True:
                    if lista_inteiros[0] < 1 or lista_inteiros[0] > 28:
                        valido = False
                if lista_inteiros[0] < 1 or lista_inteiros[0] > 29:
                    valido = False
            
        else:
            valido = False
        
    else:
        valido = False
    
    if valido == True:
        print('Data valida')
    else:
        print('Data invalida')
    
except:
    print('Digite uma data valida')