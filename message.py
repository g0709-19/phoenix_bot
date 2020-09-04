import settings

class Message:
    async def test(self):
        await self.message.channel.send('hi')

    messages = {
        f'hello {settings.BOT_NAME}': test,
    }

    def __init__(self, message):
        self.message = message
        self.function = None if message.content not in self.messages else self.messages[message.content]