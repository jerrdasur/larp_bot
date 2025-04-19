from telegram import Update
from telegram.ext import ContextTypes
from core.base_command import BaseCommand
from ..services.datastore import DataStore
from ..models.user_data import UserData

class StartCommand(BaseCommand):
    name = "start"
    description = "Зарегистрировать пользователя"

    def __init__(self, datastore: DataStore) -> None:
        self.datastore = datastore

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        user_data = UserData(
            user_id=user.id,
            username=user.username or "<unknown>",
            character_name="",
            roles=[]
        )
        self.datastore.register_user(user_data)
        await update.message.reply_text(f"Привет, {user.username}! Вы зарегистрированы.")