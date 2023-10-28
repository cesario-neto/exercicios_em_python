"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

classificacao = 0

pergunta = input('Telefonou para a vítima? ')
pergunta = pergunta.lower()
if pergunta == 'sim' or pergunta == 'não' or pergunta == 's' or pergunta == 'nao' or pergunta == 'n':
    if pergunta == 'sim' or pergunta == 's':
        classificacao += 1
    else:
        pass
        
    pergunta = input('Esteve no local do crime? ')
    pergunta = pergunta.lower()
    if pergunta == 'sim' or pergunta == 'não' or pergunta == 's' or pergunta == 'nao' or pergunta == 'n':
        if pergunta == 'sim' or pergunta == 's':
            classificacao += 1
        else:
            pass
            
        pergunta = input('Mora perto da vítima? ')
        pergunta = pergunta.lower()
        if pergunta == 'sim' or pergunta == 'não' or pergunta == 's' or pergunta == 'nao' or pergunta == 'n':
            if pergunta == 'sim' or pergunta == 's':
               classificacao += 1
            else:
                pass
            
            pergunta = input('Devia para a vítima? ')
            pergunta = pergunta.lower()
            if pergunta == 'sim' or pergunta == 'não' or pergunta == 's' or pergunta == 'nao' or pergunta == 'n':
                if pergunta == 'sim' or pergunta == 's':
                    classificacao += 1  
                else:
                    pass  
            
                pergunta = input('Já trabalhou com a vítima? ')
                pergunta = pergunta.lower()
                if pergunta == 'sim' or pergunta == 'não' or pergunta == 's' or pergunta == 'nao' or pergunta == 'n':
                    if pergunta == 'sim' or pergunta == 's':
                        classificacao += 1 
                        
                    if classificacao == 2:
                        print('Você é um Suspeito!')
                    elif classificacao == 3 or classificacao == 4:
                        print('Você é um Cúmplice!!')
                    elif classificacao == 5:
                        print('Você é um ASSASSINO!!!!')
                        print('GUARDAS!! PRENDA-O!')
                                        
                else:
                    print('Digite Sim ou Não apenas.')
            else:
                print('Digite Sim ou Não apenas.')
        else:
            print('Digite Sim ou Não apenas.')      
    else:
        print('Digite Sim ou Não apenas.')
else:
    print('Digite Sim ou Não apenas.')
    
                


    