#!/usr/bin/env python3

from ..functions import Scrapp

import discord
from discord.ext import tasks
from discord.ext import commands


class Scrapping(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    self.scrapping.start()

  @tasks.loop(minutes=10)
  async def scrapping(self, ) -> None:
    scrapp = Scrapp().get_news

    self.bot.dispatch(
      "scrapping_done", {
        "title": scrapp.title,
        "url": scrapp.url_news,
        "image": scrapp.url_image
      }
    )


async def setup(bot):
  await bot.add_cog(Scrapping(bot))
