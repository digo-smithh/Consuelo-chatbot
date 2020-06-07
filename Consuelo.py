from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import PySimpleGUI as sg
import time
import os
from random import randrange

bot= ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.portuguese')
trainer.train('chatterbot.corpus.english')
trainer.train('chatterbot.corpus.spanish')

sg.theme('BlueMono') 


layout = [  [sg.Text('     Hola, eu sou Consuelo Jiménez! Habla que eu te escuto!')],
            [sg.Image(filename=f"{os.path.dirname(os.path.realpath(__file__))}\img.png", key='image'),sg.Input(key='msg',focus=True,size=(37,20)), sg.Button("Enviar",change_submits=True,bind_return_key=True)], 
            [sg.Output(size=(50,20))]] 

window = sg.Window(' Consuelo Jiménez', layout,icon=f"{os.path.dirname(os.path.realpath(__file__))}\ico.ico")

vazio = ['pode falar.','fala que eu te escuto','Digass','Estoy aqui','I will always wait for you.','Fale! Não tenha medo!','Não vai falar nada? Então vai embora e para de encher o saco','que','to te vendooooo']
despedida = ['tchau','hasta la vista baby','bjinhos','já vai?','ai que grosseria','bj','xoxo','bye','adiós']

while True:
    button, values = window.Read()  
    message = values['msg']
    print(f"Você: {message}")
    window.FindElement('msg').Update('')
    if message == '':
        print(f'Consuelo: {str(vazio[randrange(9)])}')
    elif message.strip().lower() == 'tchau' or message.strip().lower() == 'tchau!' or message.strip().lower() == 'tchau.' or message.strip().lower() == 'tchauu' or message.strip().lower() == 'bjs' or message.strip().lower() == 'bj' or message.strip().lower() == 'bjss' or message.strip().lower() == 'bjus' or message.strip().lower() == 'bjuus' or message.strip().lower() == 'bjsss' or message.strip().lower() == 'bjssss' or message.strip().lower() == 'bjo' or message.strip().lower() == 'bjoo' or message.strip().lower() == 'bjuus' or message.strip().lower() == 'ate' or message.strip().lower() == 'até mais!' or message.strip().lower() == 'ate mais' or message.strip().lower() == 'ate!' or message.strip().lower() == 'to indo' or message.strip().lower() == 'vou embora!' or message.strip().lower() == 'vou embora' or message.strip().lower() == 'bye' or message.strip().lower() == 'adiós.' or message.strip().lower() == 'adiós' or message.strip().lower() == 'adios' or message.strip().lower() == 'adios.' or message.strip().lower() == 'xoxo' or message.strip().lower() == 'hasta la vista baby!' or message.strip().lower() == 'hasta la vista baby' or message.strip().lower() == 'bye bye' or message.strip().lower() == 'bye-bye!' or message.strip().lower() == 'goodbye' or message.strip().lower() == 'goodbye!' or message.strip().lower() == 'goodbye.' or message.strip().lower() == 'tchauzinho' or message.strip().lower() == 'tchauzinho!' or message.strip().lower() == 'flw' or message.strip().lower() == 'flww' or message.strip().lower() == 'hasta la vista' or message.strip().lower() == 'hasta la vista!': 
        print(f'Consuelo: {str(despedida[randrange(9)])}! E você que feche o programa.')
    else:
        reply = bot.get_response(message)
        print('Consuelo:', reply)
