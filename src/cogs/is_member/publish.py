#!/usr/bin/env python3

import discord
from discord.ext import commands

from dynaconf import settings


class MessageMonitor(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.channel.id != settings.CHANNEL_ID:
      return False

    await message.publish()


async def setup(bot):
  await bot.add_cog(MessageMonitor(bot))
