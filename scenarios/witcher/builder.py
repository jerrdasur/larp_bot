from telegram.ext import Application
from core.builder import Builder as BaseBuilder
from core.base_command import BaseCommand
from .commands.message_to_org import MessageToOrgCommand
from .commands.secret_phrase import SecretPhraseCommand
from .commands.reply_to_user import ReplyToUserCommand
from .commands.start import StartCommand
from .services.datastore import DataStore
from .services.role_service import RoleService
from .services.secret_phrase_service import SecretPhraseService
from .services.messaging_service import MessagingService


# TODO: connect it to bot.py
# TODO: test all commands
def create_application(token: str, datastore: DataStore) -> Application:
    """
    Создаёт и настраивает Telegram Application через базовый Builder из core.builder.
    """

    # ID чата организаторов из ENV
    admin_chat = datastore.load_admin_chat()
    if not admin_chat:
        print("Необходимо подключить чат МГ!")

    # Инициализируем сервисы

    role_service = RoleService(datastore)
    secret_service = SecretPhraseService(datastore)
    messaging_service = MessagingService(datastore)

    # Собираем команды
    commands: list[BaseCommand] = [
        StartCommand(datastore),
        MessageToOrgCommand(messaging_service),
        SecretPhraseCommand(role_service, secret_service),
        ReplyToUserCommand(messaging_service),
    ]

    # Используем общий Builder из core.builder
    builder = BaseBuilder(token, commands)
    return builder.build()