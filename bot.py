import os

from core.builder import Builder
from scenarios.witcher.builder import create_application
from scenarios.witcher.services.csv_datastore import CsvDataStore

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Отсутствует переменная окружения TELEGRAM_TOKEN")

    app = create_application(
        token=token,
        datastore=CsvDataStore(
            users_file="users.csv",
            requests_file="requests.csv",
            replies_file=f"replies.csv",
            secret_file="secrets.csv",
            admin_chat_file="admins.csv",
        )
    )

    print("Running Telegram Bot...")
    app.run_polling()
