import csv
from typing import Optional, List
from .datastore import DataStore
from ..models.user_data import UserData

class CsvDataStore(DataStore):
    """Реализация DataStore поверх CSV-файлов"""
    def __init__(
        self,
            users_file: str,
            requests_file: str,
            replies_file: str,
            secret_file: str,
            admin_chat_file: str,
    ) -> None:
        self.users_file = users_file
        self.requests_file = requests_file
        self.replies_file = replies_file
        self.secret_file = secret_file
        self.admin_chat_file = admin_chat_file

    def get_user(self, user_id: int) -> Optional[UserData]:
        with open(self.users_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row['user_id']) == user_id:
                    return UserData(
                        user_id=int(row['user_id']),
                        first_name=row['first_name'],
                        character_name=row['character_name'],
                        roles=row['roles'].split(';')
                    )
        return None

    def list_users(self) -> List[UserData]:
        users: List[UserData] = []
        with open(self.users_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(UserData(
                    user_id=int(row['user_id']),
                    first_name=row['first_name'],
                    character_name=row['character_name'],
                    roles=row['roles'].split(';')
                ))
        return users

    def get_secret_phrase(self) -> str:
        with open(self.secret_file, encoding='utf-8') as f:
            return f.read().strip()

    def save_request(self, user_id: int, text: str) -> None:
        with open(self.requests_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([user_id, text])

    def save_reply(self, user_id: int, text: str) -> None:
        with open(self.replies_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([user_id, text])

    def save_admin_chat(self, chat_id: int) -> None:
        with open(self.admin_chat_file, 'w', encoding='utf-8') as f:
            f.write(str(chat_id))

    def load_admin_chat(self) -> int:
        with open(self.admin_chat_file, encoding='utf-8') as f:
            return int(f.read().strip())