# ------------------------------------------------------------------------------------------------------------------

import discord
from discord.ext import commands

# ------------------------------------------------------------------------------------------------------------------

import nekos
import requests

# ------------------------------------------------------------------------------------------------------------------

import random

# ------------------------------------------------------------------------------------------------------------------

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, enquiry):
        answer = nekos.img("8ball")
        em = discord.Embed(
            title = "🎱 | 8ball",
            description = f"Enquiry: {enquiry}"
        )
        em.set_image(
            url=answer
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def facts(self, ctx):
        fact = nekos.fact()
        em = discord.Embed(
            title = f"🤓 | Here's your fact!\n{fact}"
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def why(self, ctx):
        whytxt = nekos.why()
        em = discord.Embed(
            title = f"❓ | Just Why?\n{whytxt}"
        )
        await ctx.send(embed=em)
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def owoify(self, ctx, message):
        url = f"https://nekos.life/api/v2/owoify?text={message}"
        response = requests.get(url)
        response.raise_for_status()
        jsonResponse = response.json()

        owoo = (jsonResponse["owo"])
        em = discord.Embed(
            title = f"OwOfied Text",
            description=f"`{owoo}`"
        )
        await ctx.send(embed=em) 
        
# ------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def meme(self, ctx):
        memeimg = meme.meme_image()
        memetitle = meme.meme_title()
        memesub = meme.meme_subreddit()
        memeauth = meme.meme_author()
        memelink = meme.meme_link()

        em = discord.Embed(
            title = f"{memetitle}"
        )
        em.set_image(
            url = memeimg
        )
        em.set_footer(
            text = f"Posted by {memeauth}"
        )
        await ctx.send(embed=em) 
        

# ------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Fun(client))
