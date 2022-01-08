import discord
import asyncio
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = "!", description = "Bot de Mouna")

@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Hello <:'))
        await asyncio.sleep(1)
        await client.change_presence(activity=discord.Game('Hello c:'))
        await asyncio.sleep(1)

@client.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} Ne met pas de liens!")
   else:
      await client.process_commands(message)

badwords = ['fdp', 'connard', 'pute']

@client.event
async def on_message(message):
   for i in badwords: # Go through the list of bad words;
      if i in message.content:
         await message.delete()
         await message.channel.send(f"{message.author.mention} Don't use that word!")
         client.dispatch('profanity', message, i)
         return # So that it doesn't try to delete the message again, which will cause an error.
   await client.process_commands(message)

@client.event
async def on_profanity(message, word):
   channel = client.get_channel(929102230957719562) # for me it's bot.get_channel(817421787289485322)
   embed = discord.Embed(title="Profanity Alert!",description=f"{message.author.name} just said ||{word}||", color=discord.Color.blurple()) # Let's make an embed!
   await channel.send(embed=embed)

@client.command()
async def Bonjour(ctx):
 await ctx.send("Bonjour !")

@client.command()
async def InfoServeur(ctx):
 serveur = ctx.guild
 nombreDeChainesTexte = len(serveur.text_channels)
 nombreDeChainesVocale = len(serveur.voice_channels)
 Description_du_serveur = serveur.description
 Nombre_de_personnes = serveur.member_count
 Nom_du_serveur = serveur.name
 message = f"Le serveur **{Nom_du_serveur}** contient *{Nombre_de_personnes}* personnes ! \nLa description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit et {nombreDeChainesVocale} salon vocaux."
 await ctx.send(message)

 

client.run('OTI4NzMxNDkyNjc3NDgwNTQ4.YddCmg._qTo6jvD_oEPg6gWici334mLNYY')