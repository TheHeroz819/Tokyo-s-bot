from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Colour
from datetime import datetime
from dateutil.tz import gettz
from discord.ext.commands import CommandNotFound
from apscheduler.triggers.cron import CronTrigger
from ..db import db



PREFIX=":"
OWNER_IDS = [987016559794987059]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		db.autosave(self.scheduler)
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

	async def print_message(self):
		channel = self.get_channel(1187725789307863133)
		
		await channel.send("Ok, this is for programming, this is a timed notification!")
	
	async def on_connect(self):
		print("Bot Connected!")

	async def on_disconnect(self):
		print("Bot disconnected!")

	async def on_error(self, err, *args, **kwargs):
		if err == "on_command_error":
			await args[0].send("Something went wrong.")
		raise

	async def on_command_error(self, ctx, exc):
		if isinstance(exc, CommandNotFound):
			pass
		elif hasattr(exc, ["original"]):
			raise exc.original
		else:
			raise exc

	async def on_ready(self):
		if not self.ready:
			self.ready=True
			self.guild= self.get_guild(1187725789307863130)
			self.scheduler.add_job(self.print_message, CronTrigger(second=15))
			self.scheduler.start()
			channel = self.get_channel(1187725789307863133)
			await channel.send("Now Online!")


			#embed= Embed(title="Now Online!", description="TK's Bot is Online!", colour=0x3D85C6, timestamp=datetime.now(tz=gettz('Asia/Kolkata')))
			#fields= [("What can I do?", "I can't do anything now!", True),
			#("Why?", "My owner needs to program me!", True),
			#("How long?", "Won't you damn wait for the developer to add commands?", False),
			#("What is the prefix?", "The Prefix is : For Example :help", False)]
			#for name, value, inline in fields:
			#	embed.add_field(name=name, value=value, inline=inline)
			#embed.set_author(name="TokyoTheTheHeroz", icon_url="https://cdn.discordapp.com/avatars/987016559794987059/0c25c9f619475ccfde468db95ab6a137.webp?size=160")
			#await channel.send(embed=embed)
			print("Bot ready!")
		else:
			print("Bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()