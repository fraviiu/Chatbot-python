# -*- coding: utf-8 -*-
#teste de chatbot  --Jarvis -- 
#teste 1 usando a biblioteca aiml.py - 25/06/2019

import telepot #classe para faser conexao com telegram 
import aiml  #classe que faz nosso bot conversar
import os
import sys
import time
import random
import datetime
from telepot.loop import MessageLoop


kernel = aiml.Kernel() #inicializa o bot
kernel.learn("simple.aiml") # Abre o arquivo principal da AIML (que faz referências aos outros).


#token do telegram fornecido pelo botfather
telegram = telepot.Bot('1284275711:AAFj5O62A5gyXBtFKet3gh5tEb8Br7njhUA') 

#funcao utilizada para receber menssagens 
def recebendoMSg(msg):
	fala = (msg['text'])
	#imprime na tela o que o usuario digitou no bot telegram
	print(fala)
	resp = kernel.respond(fala)	
	tipoMsg, tipoChat, chatID = telepot.glance(msg)
	#enviar a resposta do bot para telegram
	mensagem = telegram.sendMessage(chatID, resp)	
	#imprime a resposta na tela 
	print(resp)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

		
telegram.message_loop(recebendoMSg)

while True:
	pass

