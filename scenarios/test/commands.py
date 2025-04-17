from telegram import Update
from telegram.ext import ContextTypes

from core.base_command import BaseCommand


class UserInfoCommand(BaseCommand):
    name = 'user_info'
    description = 'Print all user information'

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Получаем словарь со всеми полями пользователя
        user_data = update.effective_user.to_dict()
        # Формируем список строк "ключ: значение"
        lines = [f"{field}: {value}" for field, value in user_data.items()]
        # Склеиваем в единый текст
        text = "\n".join(lines)
        # Отправляем пользователю
        await update.message.reply_text(text)