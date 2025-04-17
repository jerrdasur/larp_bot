from typing import Tuple

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


class BaseCommand:
   name = "base_command"
   description = "Base command"

   async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       raise NotImplementedError()

   def handler(self) -> CommandHandler:
       return CommandHandler(self.name, self.run)

   def menu_item(self) ->Tuple[str, str]:
       return self.name, self.description
