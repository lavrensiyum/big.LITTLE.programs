from urllib.request import urlopen
from lxml import etree
import discord
from datetime import datetime
import pytz

client = discord.Client()

@client.event
async def on_ready():
    print('Bot başlatıldı. seçimm')

@client.event
async def on_message(message):

    content = message.content.lower()

    if content == 'seçim':

        url = "https://www.haberler.com/secim/2023/cumhurbaskanligi-secimi/"
        html = urlopen(url).read()
        tree = etree.HTML(html)

        #Türkiye geneli açılan sandık
        element1 = tree.xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]')[0]
        #RTE
        element2 = tree.xpath('/html/body/form/div[7]/div/div[1]/div[1]/div[1]/div[1]/div[1]')[0]
        #KK
        element3 = tree.xpath('/html/body/form/div[7]/div/div[1]/div[1]/div[1]/div[2]/div[1]')[0]
        #SO
        element4 = tree.xpath('/html/body/form/div[7]/div/div[1]/div[1]/div[1]/div[3]/div[1]')[0]
        #Açılan sandık
        element5 = tree.xpath('/html/body/form/div[7]/div/div[1]/div[2]/div/div/div/div[3]/div[2]/div')[0]
        #Toplam sandık
        element6 = tree.xpath('/html/body/form/div[7]/div/div[1]/div[2]/div/div/div/div[3]/div[1]/div')[0]
        feedback = f'Türkiye Geneli Açılan Sandık: {element1.text}\nRecep Tayyip Erdoğan: {element2.text}\nKemal Kılıçdaroğlu: {element3.text}\nSinan Oğan: {element4.text}\nAçılan Sandık: {element5.text}\nToplam Sandık: {element6.text}'

        await message.channel.send(feedback, reference=message)

        timestamp = datetime.now(pytz.timezone('EST'))
        await message.channel.send(f'Güncelleme tarihi: {timestamp}')


client.run('QQQ')

