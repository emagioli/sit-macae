import telebot
import sitcalc

TOKEN = open('./token.txt','r').read()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','hello','comecar','oi'])
def send_welcome(message):
    rep = '''Olá! Escolha um dos comandos abaixo:

- Digite "linhas" para listar as linhas disponíveis para consulta.

- Digite "print [linha]" para consultar a tabela de horários desejada. 
(Ex.: print A33)

Obs.: Ainda em fase de testes.


    '''
    bot.reply_to(message,rep)

# @bot.message_handler(func=lambda msg:True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(func=lambda msg:True)
def list_lines(message):
    if('linhas' in message.text.lower()):
        linhas = sitcalc.print_lines_list()
        bot.reply_to(message, 'Linhas disponíveis para consulta:\n\n'+linhas+'\n(Digite "print XXX" para imprimir a tabela de horários da linha XXX)')
    elif('print' in message.text.lower()):
        rep = print_tabela(message)
        bot.reply_to(message, rep)
    else:
        bot.reply_to(message, 'Comando não reconhecido. Por favor, tente novamente.')

# @bot.message_handler(commands=['print'])
def print_tabela(message):
    line_code = message.text.split(' ')[1].upper()
    if (line_code in sitcalc.get_lines_list()):
        l = sitcalc.get_line(line_code)
        rep = sitcalc.generate_timetable_string(l)
    else:
        rep = 'Perdão, mas essa linha não consta nos meus registros. \nQuer tentar novamente?'
        #list_lines('linhas')

    return rep

bot.infinity_polling()