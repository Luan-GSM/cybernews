#!/usr/bin/env python3

import discord, aiohttp
from discord.ext import commands

from dynaconf import settings


class Webhook(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @property
  async def get_messages(self):
    channel = self.bot.get_channel(settings.CHANNEL_ID)
    return [msg.embeds[0].title async for msg in channel.history(limit=100)]

  @commands.Cog.listener()
  async def on_scrapping_done(self, data):
    await self.bot.wait_until_ready()

    titles = await self.get_messages
    if data.get("title") in titles:
      return False

    embed = discord.Embed(
      title=data.get("title"),
      url=data.get("url"),
      color=discord.Color(14423100)
    )

    embed.set_author(name="CanalFs0ciety")
    embed.set_thumbnail(url="https://blogger.googleusercontent.com/img/a/AVvXsEjwrKf4YKywRuIqCY95xk_ztENRYB2qp-RUTWDw_ijdPN0-AfuLl-1Q3qysquPmd5MbH32ztoCJI8M5sjGLjIM-s1OIkSxrg1edJ1PRhlx2vghU1SBO4vUWr7F-44DiY1rjTHgk1zLrcCII3HRaNEEwClMqUOB9NE7ya73Bwrkj-ox1-1FCc1deUCwH-g=s200")
    embed.set_image(url=data.get("image"))

    embed.add_field(name="Leia a notícia completa", value="[samirnews.com](%s)" %data.get("url"))
    embed.add_field(name="Torne-se um apoiador", value="[apoia.se](https://apoia.se/samirnewsapp)")
    embed.add_field(name="Acompanhe nossas redes sociais", value="[.gg/cylugh](https://discord.gg/MxcRHhDXaB)\n[samirnews.com](https://www.samirnews.com)")

    embed.set_footer(text="samirnews.com")

    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(settings.WEBHOOK_URL, session=session)
      await webhook.send(embeds=[embed])


async def setup(bot):
  await bot.add_cog(Webhook(bot))
