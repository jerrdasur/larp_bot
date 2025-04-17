import os

from core.builder import Builder
from scenarios.test.builder import commands as test_commands

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Отсутствует переменная окружения TELEGRAM_TOKEN")

    app = Builder(token=token, commands=test_commands).build()

    print("Running Telegram Bot...")
    app.run_polling()
