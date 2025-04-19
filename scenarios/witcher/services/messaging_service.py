from typing import Any
from .datastore import DataStore
from ..models.user_data import UserData


class MessagingService:
    """
    Сервис работы с сообщениями:
    - пересылает запросы участников в чат организаторов
    - сохраняет запросы и ответы
    - отправляет ответы пользователям
    """
    def __init__(
        self,
        datastore: DataStore,
    ) -> None:
        self.datastore = datastore

    def forward_to_admin(self, user_id: int, text: str) -> dict:
        """Формирует данные для пересылки в админ-чат"""
        # Возвращаем payload для команды, отправляющей сообщение в админ-чат
        user: UserData = self.datastore.get_user(user_id)
        char_name = user.character_name if user else str(user_id)

        return {"chat_id": self.datastore.load_admin_chat(), "text": f"Сообщение от {char_name}: {text}"}

    def record_request(self, user_id: int, text: str) -> None:
        self.datastore.save_request(user_id, text)

    def record_reply(self, user_id: int, text: str) -> dict:
        self.datastore.save_reply(user_id, text)
        # payload для отправки пользователю
        return {"chat_id": user_id, "text": text}