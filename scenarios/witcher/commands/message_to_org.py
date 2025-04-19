from telegram import Update
from telegram.ext import ContextTypes
from core.base_command import BaseCommand
from ..services.messaging_service import MessagingService

class MessageToOrgCommand(BaseCommand):
    name = "message"
    description = "Отправить сообщение организаторам"

    def __init__(self, messaging: MessagingService) -> None:
        self.messaging = messaging

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        text = " ".join(context.args)
        user_id = update.message.from_user.id

        # сохраняем и формируем данные для admin-чат
        self.messaging.record_request(user_id, text)
        payload = self.messaging.forward_to_admin(user_id, text)

        await update.bot.send_message(**payload)