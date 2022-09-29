from email import message
import discord
import returns

async def send_message(message,user_message):
    try:
        response = returns.handler(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
        
def running():
    TOKEN = '*'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} is Alive!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        user = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        if user_message[0]=='!':
            user_message = user_message[1:]
            await send_message(message, user_message)
        else:
            await send_message(message, user_message)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    client.run(TOKEN)
