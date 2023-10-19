from datetime import datetime as dt
from datetime import timedelta

# Linhas de interesse = A33 A41 // A31 C31A C31H C41A C41B

linhas = [
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
    }
]


def print_horarios(h_ini, freq, ciclos):
    for i in range(0, ciclos+1):
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

            print_horarios(h_ini, freq, ciclos)

            print()
            print('---'*15,)

        if (linha['frequencia_tc']):
            h_variaveis = len(linha['h_inicial_tc'][n])
            # print(f'h_variaveis = {h_variaveis}')
            # print(f'lista = {linha["h_inicial_tc"]}')
            # print(f'frequencias = {linha["frequencia_tc"]}')
            print(f'Saída Terminal Central:', end='\n\n')
            for f in range(0,h_variaveis):
                h_ini = dt.strptime(linha['h_inicial_tc'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final_tc'][n][f] + ':00', '%H:%M:%S')
                tempo_circulando = (h_fim - h_ini)
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                freq = timedelta(minutes=float(linha['frequencia_tc'][n][f].replace('min', '')))
                print_horarios(h_ini, freq, ciclos)
    print()
    print('---'*15)
    print()

for l in linhas: seeyouspacecowboy(l)