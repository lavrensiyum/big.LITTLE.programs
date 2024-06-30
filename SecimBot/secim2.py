

from urllib.request import urlopen
from lxml import etree
import discord
import datetime
import pytz # built-in, no need to install
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('Bot başlatıldı. seçimm')

@client.event
async def on_message(message):

    content = message.content.lower()

    if content == 'seçim':
        url = "https://www.haberler.com/secim/"
        #url = "https://secim.aa.com.tr/" # maalesef
        #url = "https://secim.ntv.com.tr/"
        
        html = urlopen(url).read()
        tree = etree.HTML(html)

        # "Son Güncelleme: ...."
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%d.%m.%Y %H:%M")

        #Erdoğan Yüzde
        element1 = tree.xpath('/html/body/form/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div')[0]
        #Erdoğan Oy Sayısı
        element2 = tree.xpath('/html/body/form/div[8]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span')[0]

        # -------

        #Kılıçdaroğlu Yüzde
        element3 = tree.xpath('/html/body/form/div[8]/div[1]/div[1]/div[2]/div[1]/div[2]/div')[0]
        #Kılıçdaroğlu Oy Sayısı
        element4 = tree.xpath('/html/body/form/div[8]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/span')[0]
        
        # -------

        # Oy Farkı
        element5 = tree.xpath('/html/body/form/div[8]/div[1]/div[1]/div[2]/div[2]/i')[0]
        # Açılan Sandık Oranı
        element6 = tree.xpath('/html/body/form/div[3]/div[2]/div/div[2]/div[2]')[0]
        
        print(element1.text)
        print(element2.text)
        print(element3.text)
        print(element4.text)
        print(element5.text)
        print(element6.text)
        
        feedback = f' \nErdoğan Yüzde: {element1.text}\n Erdoğan Oy Sayısı: {element2.text}\n ----\n Kılıçdaroğlu Yüzde: {element3.text}\n Kılıçdaroğlu Oy Sayısı: {element4.text}\n ----\n Açılan Sandık Oranı: {element6.text}'
        feedback2 = f'\nGüncelleme Tarihi: {formatted_time}\n Kaynak: secim.aa.com.tr'
        await message.channel.send(feedback, reference=message)
        await message.channel.send(feedback2)


client.run('QQQ')


