from telegram import Update
from telegram.ext import ContextTypes

from core.base_command import BaseCommand
from scenarios.witcher.services.datastore import DataStore


class RegisterAdminCommand(BaseCommand):
    name = "register_admin"
    description = "Зарегистрировать текущий чат как админский"

    def __init__(self, datastore: DataStore):
        self.datastore = datastore

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id

        # Сохраните chat_id куда угодно: в DataStore, файл или БД
        self.datastore.save_admin_chat(chat_id)

        await update.message.reply_text(f"Этот чат ({chat_id}) теперь считается чатом организаторов.")
