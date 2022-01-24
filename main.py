import json
from os import name
import discord
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
import random

with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']

client = commands.Bot(command_prefix=prefixo, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot online!\nID: {client.user.id}\nNome: {client.user}')

@client.command(aliases=['cara','coroa','caraoucoroa'])
async def moeda(ctx):
    var = random.randint(1,2)
    if var == 1: #cara
        await ctx.send('você tirou cara !')
    elif var == 2: #coroa
        await ctx.send('você tirou coroa!')
        
@client.command(aliases=['falar'])
async def say(ctx, *, mensagem=None):

    if mensagem is None:

         await ctx.send('EU não posso enviar mensagem no momento!')

    else:
        await ctx.message.delete()

        await ctx.send(f'{mensagem}')
 #EMBED DE BOAS VINDAS
@client.event
async def on_member_join(member):
    guild = member.guild
    canal = discord.utils.get(guild.channels, id=926938465042591764)
    embed = discord.Embed(title='olá! Bem-vindo(a)!', Color=0xff0000, description=f'{member.mention} seja bem-vindo(a) ao o servidor {guild.name} ! faça muitos amigos e ler as regras para não toma ban!')
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Quantidade de membros no servidor', value=len(guild.members))
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    await canal.send(embed=embed)


@client.command(aliases=['clean'])
async def purge(ctx, amount=11):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Não é possível executar o comando! Requer: `` Gerenciar Mensagens``') #Não é possível executar o comando! Requer Gerenciar Mensagens
        return
    amount = amount+1
    if amount > 101:
        await ctx.send('I can\'t delete more than 100 messages at a time!')
    else: 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'todas as mensagem foi deletada  {amount} messages!')


@client.event
async def on_member_remove(member):
    guild = member.guild
    canal = discord.utils.get(guild.channels, id=926938466317631502)
    embed = discord.Embed(title='ADEUS MLK (a)!', Color=0xff0000, description=f'{member.mention} infelismente vc não leu as regras do servidor {guild.name} isso nos não acitamos')
    embed.add_field(name='ID', value=member.id)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    await canal.send(embed=embed)


client.run(TOKEN)