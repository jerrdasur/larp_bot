from typing import List

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler, \
    CallbackContext

from core.base_command import BaseCommand


class Builder:
    def __init__(self, token: str, commands: List[BaseCommand]) -> None:
        self.token = token
        self.commands = commands

    def build(self) -> Application:
        app = ApplicationBuilder().token(self.token).post_init(self.post_init).build()
        self.add_handlers(app)

        return app

    async def post_init(self, application: Application) -> None:
        print("Post init")

        commands = [
                cmd.menu_item() for cmd in self.commands
            ]

        commands.append(("help", "list all commands"))

        await application.bot.set_my_commands(commands)

    def add_handlers(self, app: Application) -> None:
        for command in self.commands:
            app.add_handler(command.handler())

        app.add_handler(CommandHandler("help", self.help))

        app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.unknown_command)
        )

    @staticmethod
    async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        # update.message.text — это полный текст пришедшей команды, например "/foo"
        await update.message.reply_text(
            f"❌ Неизвестная команда: `{update.message.text}`\n"
            "Используйте /help, чтобы увидеть список доступных команд.",
            parse_mode="Markdown"
        )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        cmds = [cmd.menu_item() for cmd in self.commands]
        # Формируем список строк "ключ: значение"
        lines = [f"/{cmd}: {desc}" for cmd, desc in cmds]
        # Склеиваем в единый текст
        text = "\n".join(lines)
        # Отправляем пользователю
        await update.message.reply_text(text)