# NeoGPT Telegram Bot

Продвинутый GPT-бот в Telegram с подписками, генерацией изображений и поддержкой Webhook.

## Запуск

1. Установи зависимости:
```
pip install -r requirements.txt
```

2. Заполни `.env` или переменные среды:
- BOT_TOKEN
- BASE_URL (без https://)
- WEBHOOK_SECRET_KEY
- OPENAI_API_KEY
- MONGO_URL

3. Запусти `bot.py` или задеплой на Railway.

## Функции

- Поддержка GPT-4, GPT-4o, изображений
- Платные подписки через ЮMoney
- Ограничения и контроль сообщений
- MongoDB для хранения данных