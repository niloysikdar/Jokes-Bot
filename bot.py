from dotenv import load_dotenv
import os
import discord
from jokes import get_jokes


load_dotenv()
token = os.getenv('TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if ("joke" in message.content.lower()):
            final_joke = get_jokes()
            await message.channel.send(final_joke)


client = MyClient()
client.run(token)
