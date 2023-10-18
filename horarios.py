from datetime import datetime as dt
from datetime import timedelta

# Linhas de interesse = A33 A41 // A31 C31A C31H C41A C41B

linhas = [
    {
        'linha': 'A33',
        'nome': 'Novo Hospital',
        'h_inicial_tc': ['05:20', '06:40', '06:40'],
        'h_final_tc': ['22:40', '21:20', '21:20'],
        'frequencia_tc': ['40min', '80min', '80min'],
        'h_inicial': ['05:20', '06:00', '06:00'],
        'h_final': ['22:40', '20:40', '20:40'],
        'frequencia': ['40min', '80min', '80min'],
        'dias': ['Seg à Sex', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A73',
        'nome': 'Engenho da Praia',
        'h_inicial_tc': ['06:31', '06:30', '06:30'],
        'h_final_tc': ['23:00','20:00','20:00'],
        'frequencia_tc': ['46min', '90min', '90min'],
        'h_inicial': ['05:45','05:45','05:45'],
        'h_final': ['21:51','19:15','19:15'],
        'frequencia': ['46min', '90min', '90min'],
        'dias': ['Seg à Sex', 'Sábado', 'Domingo']
    },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
    # {'linha':,
    #     'nome':,
    #     'h_inicial_sem':,
    #     'h_final_sem':,
    #     'frequencia_sem':,
    #     'h_inicial_sab':,
    #     'h_final_sab':,
    #     'frequencia_sab':,
    #     'h_inicial_domg':,
    #     'h_final_domg':,
    #     'frequencia_domg':,
    #     },
]


def print_horarios(h_ini, freq, ciclos):
    for i in range(0, ciclos+1):
        print((h_ini + i*freq).strftime('%H:%M'), end='\t')
        if ((i+1) % 4 == 0):
            print()


linha = linhas[1]
# Calcular horários durante a semana

print(f'    Linha: {linha["nome"]} ({linha["linha"]})')
for n in range(0,len(linha['dias'])):
    print()
    print('---'*15)
    print(f'    {linha["dias"][n]}  ')
    print('---'*15)
    print(f'Saída {linha["nome"]}:', end='\n\n')

    h_ini = dt.strptime(linha['h_inicial'][n] + ':00', '%H:%M:%S')
    h_fim = dt.strptime(linha['h_final'][n] + ':00', '%H:%M:%S')

    tempo_circulando = (h_fim - h_ini)
    freq = timedelta(minutes=float(linha['frequencia'][n].replace('min', '')))

    ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())

    print_horarios(h_ini, freq, ciclos)

    print()
    print('---'*15,)

    if (linha['frequencia_tc']):
        print(f'Saída Terminal Central:', end='\n\n')

        h_ini = dt.strptime(linha['h_inicial_tc'][n] + ':00', '%H:%M:%S')
        h_fim = dt.strptime(linha['h_final_tc'][n] + ':00', '%H:%M:%S')

        tempo_circulando = (h_fim - h_ini)
        ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
        freq = timedelta(minutes=float(linha['frequencia'][n].replace('min', '')))

        print_horarios(h_ini, freq, ciclos)
