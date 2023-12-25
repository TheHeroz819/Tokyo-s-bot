from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Colour
from datetime import datetime
from dateutil.tz import gettz



PREFIX=":"
OWNER_IDS = [987016559794987059]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()
		super().__init__(
			command_prefix=PREFIX, 
			owner_ids=OWNER_IDS,
			intents=Intents.all(),
			)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)


	async def on_connect(self):
		print("Bot Connected!")

	async def on_disconnect(self):
		print("Bot disconnected!")

	async def on_ready(self):
		if not self.ready:
			self.ready=True
			print("Bot ready!")

			channel = self.get_channel(1187725789307863133)
			await channel.send("Now Online!")

			embed= Embed(title="Now Online!", description="TK's Bot is Online!", colour=0x3D85C6, timestamp=datetime.now(tz=gettz('Asia/Kolkata')))
			fields= [("What can I do?", "I can't do anything now!", True),
			("Why?", "My owner needs to program me!", True),
			("How long?", "Won't you damn wait for the developer to add commands?", False),
			("What is the prefix?", "The Prefix is : For Example :help", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_author(name="TokyoTheTheHeroz", icon_url="https://cdn.discordapp.com/avatars/987016559794987059/0c25c9f619475ccfde468db95ab6a137.webp?size=160")
			await channel.send(embed=embed)
			
		else:
			print("Bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()