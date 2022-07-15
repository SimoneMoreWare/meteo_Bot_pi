import sys
import Adafruit_DHT
import telepot

sensor = Adafruit_DHT.DHT11
pin=4

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 
    if content_type == 'text':
        bot.sendMessage(chat_id, 'Ciao, la temperatura e pari a {0:0.01f}* e umidita e del {1:0.01f}%'.format(temperature, humidity))
        
TOKEN = 'XXXXXXXXX:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)
print 'Listening ...'

import time
while 1:
    time.sleep(1)
