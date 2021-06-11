# ------------------------------------------------------------------------------------------------------------------

import api
import nekos
import requests

import Tamako
from Tamako import Tamako

# ------------------------------------------------------------------------------------------------------------------

import discord
from discord.ext import commands

# ------------------------------------------------------------------------------------------------------------------

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def cat(self, ctx):
        img = nekos.cat()
        em = discord.Embed(
            title=f"Nya!"
        )
        em.set_image(
            url=img
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def dog(self, ctx):
        img = nekos.img("woof")
        em = discord.Embed(
            title=f"Woof!"
        )
        em.set_image(
            url=img
        )
        await ctx.send(embed=em)

    @commands.command()
    async def panda(self, ctx):
        panda = Tamako.image(type="panda")
        em = discord.Embed(
            title=f"Grrrr!"
        )
        em.set_image(
            url=panda
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------
        
        
    @commands.command()
    async def bird(self, ctx):
        koala = Tamako.image(type="bird")
        em = discord.Embed(
            title=f"Tweet!"
        )
        em.set_image(
            url=koala
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Images(client))
