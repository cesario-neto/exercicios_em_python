"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do 
arquivo usando este link (em minutos).
"""

tamanho_do_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade_internet = int(input('Digite a velocidade da sua internet em Mbps: '))
tempo_de_download = (tamanho_do_arquivo / velocidade_internet) / 60

print(f'Tempo aproximado de download {tempo_de_download:.2f} minutos')


