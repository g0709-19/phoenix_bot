import json, discord, settings
from event import MyEvent
from command import MyCommand

bot = MyCommand().bot
event = MyEvent(bot)

TOKEN = settings.BOT_TOKEN
bot.run(TOKEN)