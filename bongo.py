import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'bongo cat welcomes you!!!!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='bc:help'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'bc:help':
        await client.send_message(message.channel,'Commands: \n randombongo - gives you a picture of a random bongo cat picture \n bongo - just a random command i made, haves the bot say "cat" back \n amicool - haves the bot decide if youre cool or not ')
    if message.content.startswith('bc:randombongo'):
        randomlist = ["https://pixel.nymag.com/imgs/daily/intelligencer/2018/09/24/24-bongo-cat.w700.h700.jpg", "https://cdn-01.independent.ie/world-news/and-finally/article37341486.ece/6d901/AUTOCROP/w620/ipanews_ffe4bda3-e5ae-4fe0-ac5f-bdacd5373e60_1", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLy27yV-Ly47ryWsN10qIoAokDuNRE_qMTsUBlByjU3qgRVL9x", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA4zxxFESK4q7AUl3kbVEOdL7onoBUdwKGYicYazZcbz2QEfOb", "https://derpicdn.net/img/2018/9/17/1834650/full.gif"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('bc:amicool'):
        randomlist = ["yes u cool", "no ur not cool"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'bc:bongo':
        await client.send_message(message.channel,'cat')
client.run('NTE1NjkyMDQ5NDkyNjA3MDA3.DtozyQ.3ghAIAWFLMtI9IQwWMJ9y64H8Xw')
