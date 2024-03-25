import telebot
import sitcalc
from datetime import datetime

TOKEN = open('./token.txt','r').read()

bot = telebot.TeleBot(TOKEN)

standard_rep = '''Olá! Eu sou o bot dos horários de ônibus SIT Macaé (não oficial). 
    
Por favor, DIGITE um dos comandos abaixo:

- linhas : lista as linhas disponíveis para consulta.

- print [linha] : consultar a tabela de horários desejada. 

(Exemplo: print A33)

Contato: enzomagioli.pro@gmail.com
    '''

@bot.message_handler(commands=['start','hello','comecar','oi'])
def send_welcome(message):
    rep = standard_rep
    bot.reply_to(message,rep)

@bot.message_handler(func=lambda msg:True)
def list_lines(message):
    print(f'{datetime.now()}: "{message.text}"')
    print()
    text = message.text.lower()
    if('linhas' in text):
        linhas = sitcalc.print_lines_list()
        bot.reply_to(message, 'Linhas disponíveis¹ para consulta:\n\n'+linhas+'\n(Digite "print XXX" para imprimir a tabela de horários da linha XXX)\n\n ¹ Apenas linhas do Terminal Central.')
    elif('print' in text):
        rep = print_tabela(message)
        bot.reply_to(message, rep)
    elif('see you' in text):
        rep = 'See you space cowboy...'
        bot.reply_to(message, rep)
    else:
        rep = standard_rep
        bot.reply_to(message, rep)

def print_tabela(message):
    line_code = message.text.split(' ')[1].upper()
    if (line_code in sitcalc.get_lines_list()):
        l = sitcalc.get_line(line_code)
        rep = sitcalc.generate_timetable_string(l)
    else:
        rep = 'Perdão, mas essa linha não consta nos meus registros. \nQuer tentar novamente?'

    return rep

print(f'Início da execução: {datetime.now()}')

bot.infinity_polling()