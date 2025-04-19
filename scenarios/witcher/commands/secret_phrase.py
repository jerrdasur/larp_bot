from telegram import Update
from telegram.ext import ContextTypes
from core.base_command import BaseCommand
from ..services.role_service import RoleService
from ..services.secret_phrase_service import SecretPhraseService

class SecretPhraseCommand(BaseCommand):
    name = "secret"
    description = "Ввести секретную фразу"

    def __init__(
        self,
        role_service: RoleService,
        secret_service: SecretPhraseService,
    ) -> None:
        self.role_service = role_service
        self.secret_service = secret_service

    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_id = update.effective_user.id
        if not self.role_service.has_role(user_id, "vip"):
            await update.message.reply_text("❌ Недостаточно прав")
            return

        phrase = " ".join(context.args)
        if self.secret_service.validate(phrase):
            await update.message.reply_text("🎉 Фраза верна!")
        else:
            await update.message.reply_text("❌ Неверная фраза")