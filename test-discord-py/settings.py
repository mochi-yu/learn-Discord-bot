# 環境変数の取得 ########
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)   # .envが見つからないときにエラー

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("BOT_TOKEN")
########################


# Intentの設定 ##########
import discord

myIntents = discord.Intents(
  members=True,
  emojis_and_stickers=True,
  invites=True,
  messages=True,
  reactions=True,
  message_content=True,
  guild_scheduled_events=True,
)
#########################