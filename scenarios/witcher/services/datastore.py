from abc import ABC, abstractmethod
from typing import Optional
from ..models.user_data import UserData

class DataStore(ABC):
    """Интерфейс для доступа к данным участников, секретной фразы и сообщений."""

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[UserData]:
        """Возвращает данные пользователя по user_id или None, если не найден."""
        pass

    @abstractmethod
    def register_user(self, user_data: UserData) -> None:
        pass

    @abstractmethod
    def list_users(self) -> list[UserData]:
        """Возвращает список всех зарегистрированных пользователей."""
        pass

    @abstractmethod
    def get_secret_phrase(self) -> str:
        """Возвращает текущую секретную фразу для проверки."""
        pass

    @abstractmethod
    def save_request(self, user_id: int, text: str) -> None:
        """Сохраняет запрос участника для последующей обработки организаторами."""
        pass

    @abstractmethod
    def save_reply(self, user_id: int, text: str) -> None:
        """Сохраняет ответ организатора для последующей отправки пользователю."""
        pass

    @abstractmethod
    def save_admin_chat(self, chat_id: int) -> None:
        """Сохраняет id чата МГ"""
        pass

    @abstractmethod
    def load_admin_chat(self) -> int:
        """Возвращает id чата МГ"""
        pass