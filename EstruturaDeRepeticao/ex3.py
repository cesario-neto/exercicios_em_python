"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input('Digite o seu nome: ')
    while len(nome) < 3:
        print('Seu nome deve possuír mais de 3 caracteres. ')
        nome = input('Digite o seu nome: ')
        
    idade = int(input('Digite sua idade: '))
    while idade < 0 or idade > 150:
        print('Sua idade dever ser maior que 0 e menor que 150. ')
        idade = int(input('Digite sua idade: '))
    
    salario = input('Digite seu salário: ')
    salario = salario.replace(',', '.')
    while float(salario) < 0.00:
        print('Seu salário não pode ser menor que R$0,00')
        salario = input('Digite seu salário: ')
        salario = salario.replace(',', '.')
    
    sexo = input('Digite seu sexo (f) ou (m): ')
    sexo = sexo.lower()
    
    while sexo != 'f' and sexo != 'm':
        print('sexo inválido')
        sexo = input('Digite seu sexo (f) ou (m): ')
        sexo = sexo.lower()
    
    estado_civil = input('Digite o seu estado civil (s = solteiro(a)), (c = casado(a)), (v = viúvo(a)), (d = divorciado(a)): ')
    estado_civil = estado_civil.lower()
    
    while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        print('Estado civil inválido.')
        estado_civil = input('Digite o seu estado civil (s = solteiro(a)), (c = casado(a)), (v = viúvo(a)), (d = divorciado(a)): ')
        estado_civil = estado_civil.lower()
    
    print(f'\nNome: {nome}\nIdade: {idade}\nSalario: R${salario}\nSexo: {sexo}\nEstado Civil: {estado_civil}')
    break