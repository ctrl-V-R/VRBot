from random import randint
from secrets import randbelow


def handler(message):
    user_message = message.lower()
    
    ## Help page #############################################################################################################################################################
    if user_message == 'help':
        f = open('commands.txt', 'r')
        command_list = f.read()
        f.close()
        return str("`Here is a list of my Commands:\n" + command_list + "`")
    ## Commands #############################################################################################################################################################
    if user_message == 'hello' or user_message == 'hi' or user_message == 'hey':
        return 'Hello :D'
    
    if user_message == 'dice' or user_message == 'roll':
        return str(randint(1,6))
    
    if user_message == 'flip' or user_message == 'toss' or user_message == 'coin':
        if randint(0,1):return 'Heads' 
        else: return 'Tails' 