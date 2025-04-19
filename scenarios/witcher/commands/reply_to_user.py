from telegram import Update
from telegram.ext import ContextTypes
from core.base_command import BaseCommand
from ..services.messaging_service import MessagingService

class ReplyToUserCommand(BaseCommand):
    name = "reply"
    description = "Ответить участнику"

    def __init__(self, messaging: MessagingService) -> None:
        self.messaging = messaging

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # бот получает reply в админ-чате
        if not update.message.reply_to_message:
            await update.message.reply_text("Ответьте на сообщение пользователя в админ-чате.")
            return

        original = update.message.reply_to_message
        user_id = int(original.text.split()[2].rstrip(':'))  # парсинг из текста admin-уведомления
        text = update.message.text

        # сохраняем и готовим payload для пользователя
        payload = self.messaging.record_reply(user_id, text)
        await update.bot.send_message(**payload)
        await update.message.reply_text("Ответ отправлен пользователю.")