import os
import random

import qrcode
import telebot
from telebot import *

token = '5768245357:AAGMh04C5CPh0btcIbk2302T1gU38YPWLBo'

bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f"Привет я новый бот который сгенерируют qr code сайта. Отправте ссылку сайта Пример: http://example.com/")

        
@bot.message_handler()

def get_qrcode(message):
    
    if "http" in  f'{message}':
        pass
    else:
        bot.send_message(message.chat.id,f"Отправте ссылку! Пример: http://example.com/")
        raise 
        
        
    name_file = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(5)))

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f'{name_file }.jpeg', 'JPEG')

    photo = open(f'{name_file }.jpeg', 'rb')

    bot.send_photo(message.chat.id, photo, caption='Ловите...')

    os.system(f'sudo rm -f {name_file }.jpeg')

bot.infinity_polling()
