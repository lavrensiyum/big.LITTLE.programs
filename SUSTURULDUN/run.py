import discord
from datetime import datetime
import pytz


yildiz = ['<@30103__________>', '<@1071___________>'] # ben ve botun id'si


###### Hugging Face #####
# https://huggingface.co/savasy/bert-base-turkish-sentiment-cased

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")

def ml_model(text):
    pipe = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)
    return pipe(text)[0]['label']

#########################

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot başlatıldı. susturuldun!')

@client.event
async def on_message(message):
      
    content = message.content.lower()
    content_split = message.content.split()

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    #target_server = str(client.get_channel)
    server_name = str(message.guild.name)

#### If someone __mentions__ me or bot
    for word in yildiz:
        if word in content_split:        
            result = ml_model(content)
            
            if result == 'negative':
                print(f'DELETED: {server_name}-{channel}| {username}: {user_message}')
                await message.delete()
####

#### If someone __replies__ to me or bot
    if message.reference is None:
        return
    
    try:
        referenced_message_id = message.reference.message_id
        referenced_message = await message.channel.fetch_message(referenced_message_id)
        author = referenced_message.author
    except discord.NotFound:
        return
    
    author_id = str(author.id)
    
    if author_id in yildiz:
        
        content = message.content.lower()
        content = str(content)
        result = ml_model(content)
        
        if result == 'negative': 
            await message.delete()
            print(f'DELETED: {server_name}-{channel}| {username}: {user_message}')
                
    timestamp = datetime.now(pytz.timezone('EST'))
    #print(f'{server_name}-{channel}| {username}: {user_message}')

    return


client.run('__TOKEN__')