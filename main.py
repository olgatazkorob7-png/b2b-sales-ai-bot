import os
import staypresent

# Настраиваем веб-сервер для Koyeb
staypresent.web.json({"status": "running"})

# Запускаем наш файл с ботом (bot.py)
staypresent.run(
    "bot.py",
    port=int(os.getenv("PORT", 8080))
)
