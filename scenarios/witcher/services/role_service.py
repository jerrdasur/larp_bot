from typing import List
from .datastore import DataStore

class RoleService:
    def __init__(self, datastore: DataStore):
        self.datastore = datastore

    def has_role(self, user_id: int, role: str) -> bool:
        user = self.datastore.get_user(user_id)
        return role in (user.roles if user else [])
