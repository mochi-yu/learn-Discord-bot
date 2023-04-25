import discord
import discord.app_commands

from settings import TOKEN, myIntents

client = discord.Client(intents=myIntents)
tree = discord.app_commands.CommandTree(client)

@tree.command(
  name="yeah",
  description="Say yeah reply.",
)
async def hoge(ctx: discord.Interaction):
  await ctx.response.send_message("Yeah...!!")

@client.event
async def on_ready():
  print("Log in.")
  await tree.sync()

@client.event
async def on_message(message):
  print(f'Message from {message.author}: {message.content}')

  if not message.author.bot:
    if message.content == '/python':
      await message.channel.send("Python!!")
    # else:
    #   await message.channel.send("Hello!")


# リアクションが追加されたとき
@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
  print(payload.member.name + "：リアクション" + payload.emoji.name + " が追加されました")

  role_list = await payload.member.guild.fetch_roles()

  # 特定のメッセージに付けられたリアクションだけに適用
  if payload.message_id == 1099371259571212318:
    # 付与するロールを取得して付与する
    if payload.emoji.name == "🟢":
      role: discord.role.Role = discord.utils.get(role_list, name="role1")
      await payload.member.add_roles(role)
      print("ロールを追加しました")
    elif payload.emoji.name == "🟣":
      role: discord.role.Role = discord.utils.get(role_list, name="role2")
      await payload.member.add_roles(role)
      print("ロールを追加しました")
    elif payload.emoji.name == "❌":
      # ×のリアクションをしたユーザのロールを取り消す
      remove_roles = [
        discord.utils.get(role_list, name="role1"),
        discord.utils.get(role_list, name="role2")
      ]
      await payload.member.remove_roles(*remove_roles)
      print("ロールをリセットしました")

      # ✖のリアクションをしたユーザのリアクションを取り消す
      ch: discord.TextChannel = await payload.member.guild.fetch_channel(payload.channel_id)
      print("メッセージのあるチャンネルを取得しました。")
      msg: discord.Message = await ch.fetch_message(payload.message_id)
      print("対象のメッセージを取得しました。")
      # reactions: list[discord.Reaction] = await msg.reactions
      for r in msg.reactions:
        if r.emoji != "❌":
          await msg.remove_reaction(r, payload.member)
        elif r.emoji == "❌":
          removeEmojiReaction = r
      await msg.remove_reaction(removeEmojiReaction, payload.member)
      print('リアクションを除去しました')
    else:
      print("関係の無いリアクションが追加されました。")






client.run(TOKEN)