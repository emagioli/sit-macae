from datetime import datetime as dt
from datetime import timedelta

import math

# Linhas de interesse = A33 A41 // A31 C31A C31H C41A C41B

lista = [
    {
        'linha': 'A33',
        'nome': 'Novo Hospital',
        'h_inicial_tc': [['05:20'], ['06:40'], ['06:40']],
        'h_final_tc': [['22:40'], ['21:20'], ['21:20']],
        'frequencia_tc': [['40min'], ['80min'], ['80min']],
        'h_inicial': [['05:20'], ['06:00'], ['06:00']],
        'h_final': [['22:40'], ['20:40'], ['20:40']],
        'frequencia': [['40min'], ['80min'], ['80min']],
        'dias': ['Seg à Sex', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A73R',
        'nome': 'Engenho da Praia (Rápido)',
        'h_inicial_tc': [['06:31', '21:05', '22:00'], ['06:30'], ['06:30']],
        'h_final_tc': [['21:05', '22:00', '23:00'], ['20:00'], ['20:00']],
        'frequencia_tc': [['46min', '55min', '60min'], ['90min'], ['90min']],
        'h_inicial': [['05:45'], ['05:45'], ['05:45']],
        'h_final': [['21:51'], ['19:15'], ['19:15']],
        'frequencia': [['46min'], ['90min'], ['90min']],
        'dias': ['Seg à Sex', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A73',
        'nome': 'Engenho da Praia',
        'h_inicial_tc': [['06:10', '06:48', '07:14', '19:30', '20:50', '21:40'], ['06:30'], ['06:30']],
        'h_final_tc': [['06:48', '07:14', '19:30', '20:50', '21:40', '22:20'], ['20:00'], ['20:00']],
        'frequencia_tc': [['38min', '26min', '32min', '40min', '50min', '40min'], ['90min'], ['90min']],
        'h_inicial': [['05:22', '06:08', '06:26', '19:14', '20:00'], ['07:15'], ['07:15']],
        'h_final': [['06:08', '06:26', '19:14', '20:00', '21:20'], ['20:45'], ['20:45']],
        'frequencia': [['46min', '18min', '32min', '46min', '40min'], ['90min'], ['90min']],
        'dias': ['Seg à Sex', 'Sábado', 'Domingo']
    },
    {
    'linha': 'A31',
    'nome': 'Terminal Central X Vila Moreira',
    'h_inicial_tc': [['06:00', '17:00', '20:00', '23:30'], ['06:20'], ['06:20']],
    'h_final_tc': [['17:00', '20:00', '23:30', '00:00'], ['23:20'], ['23:20']],
    'frequencia_tc': [['30min', '36min', '30min', '30min'], ['40min'], ['40min']],
    'h_inicial': [['05:15', '16:45', '17:18', '19:42', '20:15', '23:15'], ['05:40', '22:40'], ['05:40', '22:40']],
    'h_final': [['16:45', '17:18', '19:42', '20:15', '23:15', '00:00'], ['22:40', '00:00'], ['22:40', '00:00']],
    'frequencia': [['30min', '33min', '36min', '33min', '30min', '45min'], ['40min', '80min'], ['40min', '80min']],
    'dias': ['Dias Úteis', 'Sábados', 'Domingos e Feriados']
}
]

##selecione as linhas desejadas abaixo

linhas = [lista[2]]


def print_horarios(h_ini, h_fim, freq, ciclos):
    if(ciclos < 2): ciclos +=1
    for i in range(0, ciclos+1):
        if (h_ini + i*freq) < h_fim:
            print((h_ini + i*freq).strftime('%H:%M'), end='\t')
            if ((i+1) % 4 == 0):
                print()
    print()

# Calcular horários durante a semana

def seeyouspacecowboy(linha):
    print(f'    Linha: {linha["nome"]} ({linha["linha"]})')
    for n in range(0, len(linha['dias'])):
        print()
        print('---'*15)
        print(f'    {linha["dias"][n]}  ')
        print('---'*15)
        print(f'Saída {linha["nome"]}:', end='\n\n')

        h_variaveis = len(linha['h_inicial'][n])
        for f in range(0, h_variaveis):
            h_ini = dt.strptime(linha['h_inicial'][n][f] + ':00', '%H:%M:%S')
            h_fim = dt.strptime(linha['h_final'][n][f] + ':00', '%H:%M:%S')
            tempo_circulando = (h_fim - h_ini)
            freq = timedelta(minutes=float(
                linha['frequencia'][n][f].replace('min', '')))
            ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
            print_horarios(h_ini, h_fim, freq, ciclos)

        if (linha['frequencia_tc']):
            print()
            print('---'*15,)
            print(f'Saída Terminal Central:', end='\n\n')
            
            h_variaveis = len(linha['h_inicial_tc'][n])
            for f in range(0,h_variaveis):
                h_ini = dt.strptime(linha['h_inicial_tc'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final_tc'][n][f] + ':00', '%H:%M:%S')
                #print(h_fim) ## para debugging
                tempo_circulando = (h_fim - h_ini)
                freq = timedelta(minutes=float(linha['frequencia_tc'][n][f].replace('min', '')))
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                print_horarios(h_ini, h_fim, freq, ciclos)
    

for l in linhas: 
    seeyouspacecowboy(l) 
    print()
    print('---'*15)
    print()