from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

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
			await channel.send("Now Online! <@987016559794987059> Sleep now!")

		else:
			print("Bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()