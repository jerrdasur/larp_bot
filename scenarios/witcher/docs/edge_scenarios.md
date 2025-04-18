# Пограничные сценарии (edge cases)

Ниже перечислены сценарии, позволяющие проверить устойчивость бота к нестандартным ситуациям.

## 1. Пустой аргумент команды

- Отправить `/message` без текста или `/secret` без фразы.
- **Ожидаемое**: бот отвечает с инструкцией по правильному использованию команды.

## 2. Не зарегистрированный пользователь

- Не существующий `user_id` (DataStore возвращает `None`) вызывает `/message` или `/secret`.
- **Ожидаемое**: бот отвечает "Пользователь не найден" или аналогично, и не падает с ошибкой.

## 3. Ошибка чтения/записи CSV

- Повреждён или отсутствует CSV-файл (users, requests, replies, secret, admin_chat).
- **Ожидаемое**: бот логгирует ошибку и отправляет участнику/организатору понятное сообщение об ошибке, без краха.

## 4. Некорректный формат CSV

- Строка CSV не соответствует ожидаемым полям (нет `character_name` или `roles`).
- **Ожидаемое**: бот пропускает некорректные записи и логгирует предупреждение.

## 5. Одновременные записи (конкуренция)

- Два пользователя одновременно отправляют `/message`.
- **Ожидаемое**: обе записи корректно сохраняются, без потери данных.

## 6. Отсутствие роли VIP

- Пользователь с пустым списком `roles` отправляет `/secret`.
- **Ожидаемое**: бот отвечает "Недостаточно прав".

## 7. Админ‑чат не настроен

- `ADMIN_CHAT_ID` не задан в ENV при старте.
- **Ожидаемое**: бот при инициализации падает с понятным RuntimeError "ADMIN_CHAT_ID не задан в окружении".

## 8. Неявный reply в админ-чате

- Организатор отправляет `/reply` не как reply на пересланное сообщение.
- **Ожидаемое**: бот отвечает "Ответьте на сообщение пользователя в админ-чате.".

## 9. Длинные сообщения

- Пользователь или организатор отправляет очень длинный текст (>4096 символов).
- **Ожидаемое**: бот корректно разбивает на части или отвечает об ограничении длины.

## 10. Перезапуск бота

- Бот перезапускается между операциями.
- **Ожидаемое**: запуск без ошибок, данные из CSV сохраняются и доступны для новых команд.

## 11. Несуществующий user_id при ответе

- В админ-чате организатор делает reply на сообщение, внутри которого user_id не распарсился (например, формат текста изменился).
- **Ожидаемое**: бот отвечает "Не удалось определить пользователя" и логгирует проблему.

## 12. Зависание при подключении бекенда

- Backend (например, база данных) недоступен.
- **Ожидаемое**: бот отдаёт timeout/error до старта или при выполнении команд, логгирует и не падает неконтролируемо.

