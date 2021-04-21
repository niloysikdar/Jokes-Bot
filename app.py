from dotenv import load_dotenv
import discord
import os

load_dotenv()
token = os.getenv('TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if ("joke" in message.content):
            await message.channel.send("Wait \nand see")


client = MyClient()
client.run(token)
