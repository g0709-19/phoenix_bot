import discord, json

BOT_NAME = '피닉스'
DEVELOPER = '이승준'
ADMIN_ROLE = '운영진'
MAIN_COLOR = 0xFF0000

with open('secrets.json') as json_file:
    json_object = json.load(json_file)
    BOT_TOKEN = json_object['BOT_TOKEN']

COMMAND_PREFIX = '!'
BOT_STATUS = discord.Status.online
BOT_ACTIVITY = discord.Game(f'{COMMAND_PREFIX}도움말')
BOT_HELP_COMMAND = None