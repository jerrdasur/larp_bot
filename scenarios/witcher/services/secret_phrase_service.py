from ..services.datastore import DataStore

class SecretPhraseService:
    """Сервис валидации секретной фразы через DataStore"""
    def __init__(self, datastore: DataStore):
        self.datastore = datastore

    def validate(self, phrase: str) -> bool:
        # подтягиваем текущую фразу из хранилища
        secret = self.datastore.get_secret_phrase()
        return phrase == secret