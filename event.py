import discord
from message import Message

class MyEvent:
    def __init__(self, bot):
        
        @bot.event
        async def on_ready():
            print(f'we have logged in as {bot.user}')

        @bot.event
        async def on_message(message):
            # 이거 안 해주면 command 와 충돌
            if message.content.startswith(bot.command_prefix):
                await bot.process_commands(message)

            if message.author == bot.user:
                return

            msg = Message(message)
            if msg.function is not None:
                await msg.function(msg)
