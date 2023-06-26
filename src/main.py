#!/usr/bin/env python3

import logging
import discord, os
from dynaconf import settings
from discord.ext import commands

STATUS = settings.STATUS


class Bot(commands.Bot):
  def __init__(self) -> None:
    log = logging.getLogger("discord.gateway")
    log.setLevel(logging.WARNING)

    with settings.using_env(STATUS):
      super().__init__(
        command_prefix=settings.PREFIX,
        help_command=None,
        intents=discord.Intents.all()
      )


  async def load(self, bot, path: list):
    for dir in path:
      dirI = dir.replace(".", "/")
      if not os.path.exists(dirI):
        raise FileNotFoundError(
          "Nenhum diretório nomeado '%s' foi encontrado."
          %(dir)
        )

      for file in os.listdir(dirI):
        if file.endswith(".py"):
          await bot.load_extension(
            "%s.%s"
            %(dir, file[:-3])
          )


  async def setup_hook(self) -> None:
    await self.load(self, settings.COGS)

    self.tree.copy_global_to(guild=discord.Object(id=settings.SERVER_ID))
    await self.tree.sync()


  async def on_ready(self):
    print("Bot on-line. (nome: %s)" %self.user)

    await self.change_presence(
      status=discord.Status.dnd,
      activity=discord.Game(
        name=settings.NAME,
        type=3
      )
    )


bot = Bot()
with settings.using_env(STATUS):
  bot.run(settings.TOKEN)
