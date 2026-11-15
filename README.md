# 🤖 AI Sales Assistant (B2B Telegram Bot)

Умный ассистент для отдела продаж, который экономит время менеджеров и берет на себя рутину. Бот использует современные LLM и технологию **Tool Calling (Function Calling)** для взаимодействия с внутренними системами компании (CRM).

## 💡 Бизнес-ценность
Менеджеры по продажам тратят до 30% времени на переключение между CRM, почтой и мессенджерами. Этот бот становится единым окном:
*   **Мгновенная сводка по лидам:** Больше не нужно искать данные в таблицах. Бот сам обращается к базе и выдает список горячих клиентов.
*   **Генерация follow-up писем:** Бот пишет персонализированные письма клиентам на основе контекста (например, если клиент просит скидку).

## ⚙️ Ключевые фичи
*   **Tool Calling:** Нейросеть (Gemini 1.5 Flash) анализирует запрос пользователя и **сама решает**, когда нужно вызвать функцию для получения данных из CRM, а когда просто ответить текстом.
*   **Современный асинхронный стек:** Написан на Python с использованием `aiogram 3`.
*   **Защита данных:** Все ключи хранятся в переменных окружения.

## 🛠 Стек технологий
*   **Python 3.10+**
*   **aiogram 3.13** (Асинхронный фреймворк для Telegram)
*   **Google Gemini API** (LLM с поддержкой Function Calling)
*   **python-dotenv** (Управление переменными окружения)

## 🚀 Как запустить локально

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/olgatazkorob7-png/b2b-sales-ai-bot.git
   cd b2b-sales-ai-bot
Установите зависимости:

bash
pip install -r requirements.txt
Создайте файл .env в корне проекта и добавьте ваши ключи:

env
BOT_TOKEN=ваш_токен_от_BotFather
GEMINI_API_KEY=ваш_ключ_от_Google

Анализ ситуации:

Пользователь создает файл .env.example в репозитории b2b-sales-ai-bot.

Вместо текста-заглушки (например, BOT_TOKEN=ваш_токен) пользователь вставил настоящие секретные ключи (токен Telegram-бота и API-ключ Google Gemini).

GitHub сработал умно: он обнаружил паттерны секретных ключей (Secret Scanning) и заблокировал коммит, выдав предупреждение: "В результате сканирования секрета в строке 2 был обнаружен ключ API GCP...".

GitHub предлагает варианты: "Он используется в тестах", "Ложноположительный результат", "Я исправлю это позже" и кнопку "Разрешить секретный доступ" (что делать КАТЕГОРИЧЕСКИ НЕЛЬЗЯ).

Оценка рисков:

Это реальные ключи. Если они попадут в публичный репозиторий, злоумышленники могут украсть токен бота (и угнать его) или API-ключ Gemini (и потратить лимиты/деньги пользователя).

Даже если пользователь нажмет "Я исправлю это позже" и сделает коммит, ключи навсегда останутся в истории коммитов.

Формулировка плана действий для пользователя:

СТОП! Не нажимать зеленую кнопку "Разрешить секретный доступ".

Очистить файл: удалить эти ключи из поля ввода.

Вставить правильные значения: именно заглушки (ваш_токен...), как я и писал изначально.

Объяснить, почему так: .env.example нужен только для примера. Настоящие ключи идут в Render в разделе Environment Variables.

Дополнительная безопасность: посоветовать перевыпустить (отозвать) эти ключи, так как они уже засветились на скриншоте (хотя бы для успокоения, но лучше настоятельно рекомендовать). Стоп, скриншот был отправлен мне в чат. Ключи видны мне. Значит, они скомпрометированы. Нужно обязательно сказать пользователю их удалить/перевыпустить.

Пошаговая инструкция:

Отменить текущий коммит (нажать "Отмена" в модальном окне).

Удалить строки с ключами.

Вставить текст-заглушку.

Сделать коммит заново.

Сгенерировать новые токены.

Тон общения: Спокойный, но строгий в отношении безопасности. Объяснить, что это не ошибка кода, а защитный механизм GitHub.

СТОП! Ни в коем случае не нажимайте «Разрешить секретный доступ»!

GitHub сработал как отличная система безопасности и спас вас от крупной кражи. Вы вставили в файл настоящие, реальные ключи (токен вашего бота и API-ключ от Google).

Если вы нажмете зеленую кнопку, эти ключи попадут в публичный доступ. Любой хакер сможет найти их в вашем открытом репозитории, угнать вашего бота, рассылать спам от его имени или потратить все ваши деньги на запросы к Gemini.

В файл .env.example (пример) нужно вставлять только текст-заглушку, а не реальные ключи. Настоящие ключи мы потом введем в настройках Render, где они будут надежно зашифрованы.

🛠 Что нужно сделать прямо сейчас:
В открывшемся окне нажмите кнопку «Отмена» (Cancel).

В поле для текста удалите обе эти строки с вашими ключами.

Вставьте вместо них ровно этот текст-заглушку (скопируйте его):

text
BOT_TOKEN=твой_токен_от_BotFather
GEMINI_API_KEY=твой_ключ_от_Google
Теперь снова нажмите зеленую кнопку «Commit changes...» (Зафиксировать изменения).

🚨 ВАЖНО: Ваши ключи засветились!
Так как вы прислали скриншот с настоящими ключами, они теперь видны (в том числе и мне в чате). В целях безопасности их нужно перевыпустить:

Токен Telegram-бота: Идите в Telegram к @BotFather, напишите /revoke, выберите вашего бота и получите новый токен. Старый сразу перестанет работать.

Ключ Gemini: Зайдите в Google AI Studio, удалите старый ключ и создайте новый.

Новые ключи мы потом вставим в Render (в разделе Environment Variables). В коде и на GitHub их быть не должно!

Сделайте отмену, вставьте заглушку, сохраните файл и напишите мне, когда закончите.

сделала,напиши readmt
Analyze the User's Request:

User successfully fixed the .env.example file (replaced real keys with placeholders).

User is asking for the README.md content for the new repository (b2b-sales-ai-bot).

Context: We are building an AI Sales Assistant Telegram bot with Tool Calling (simulating CRM access) using Python, aiogram, and Gemini API. The goal is to showcase this as a top-tier B2B portfolio piece.

Determine the Goal of the README:

A good README for a portfolio project needs to be impressive to both technical recruiters and potential business clients.

It should explain what the bot is, why it's valuable (business value), how it works (technical stack), and how to run it.

Since it's a B2B sales bot, the language should be professional and focus on efficiency and ROI.

Structure of the README:

Title & Badges (Professional touch: Python, aiogram, Gemini).

Description (What it does, the business problem it solves).

Key Features (Tool Calling, CRM simulation, AI text generation).

Tech Stack (Python, aiogram, Gemini API).

How it works (Architecture / Workflow).

Installation & Setup (How to run locally).

Deployment (Mentioning Render).

Drafting the Content (in Russian, as requested):

Title: 🤖 AI Sales Assistant (B2B Telegram Bot)

Tagline: Умный ассистент для отдела продаж с использованием Tool Calling (Function Calling) и LLM.

Business Value: Saves time, automates routine, helps managers generate leads and follow-ups.

Features:

📊 Запрос данных из CRM (имитация).

✍️ Генерация follow-up писем.

🧠 Использование Tool Calling (Gemini сам понимает, когда нужно вызвать функцию, а когда просто ответить).

Stack: Python 3.10+, aiogram 3, Google Gemini 1.5 Flash, python-dotenv.

Setup: git clone, pip install -r requirements.txt, create .env, run python main.py.

Refining the Tone:

Make it sound like a real product. Use emojis.

Emphasize the modern architecture (Tool Calling is a hot keyword in AI right now).

Actionable Advice:

Tell the user where to paste it (in the README.md file on GitHub).

Instruct them on how to create the README.md file (if they haven't already, though GitHub usually creates it by default when initializing with a README, but they might have skipped it).

Отлично, что вы быстро среагировали и убрали настоящие ключи! Безопасность превыше всего.

Теперь давайте создадим файл README.md. В GitHub это «лицо» вашего проекта. Когда заказчик или HR зайдет в репозиторий, он первым делом прочитает именно его. Давайте сделаем так, чтобы это выглядело профессионально и дорого.

🛠 Как добавить README:
На главной странице вашего репозитория b2b-sales-ai-bot нажмите «Add file» -> «Create new file».

В поле имени файла напишите: README.md

Вставьте в большое поле следующий текст (я подготовил его с акцентом на бизнес-ценность и техническую крутость):

markdown
# 🤖 AI Sales Assistant (B2B Telegram Bot)

Умный ассистент для отдела продаж, который экономит время менеджеров и берет на себя рутину. Бот использует современные LLM и технологию **Tool Calling (Function Calling)** для взаимодействия с внутренними системами компании (CRM).

## 💡 Бизнес-ценность
Менеджеры по продажам тратят до 30% времени на переключение между CRM, почтой и мессенджерами. Этот бот становится единым окном:
*   **Мгновенная сводка по лидам:** Больше не нужно искать данные в таблицах. Бот сам обращается к базе и выдает список горячих клиентов.
*   **Генерация follow-up писем:** Бот пишет персонализированные письма клиентам на основе контекста (например, если клиент просит скидку).

## ⚙️ Ключевые фичи
*   **Tool Calling:** Нейросеть (Gemini 1.5 Flash) анализирует запрос пользователя и **сама решает**, когда нужно вызвать функцию для получения данных из CRM, а когда просто ответить текстом.
*   **Современный асинхронный стек:** Написан на Python с использованием `aiogram 3`.
*   **Защита данных:** Все ключи хранятся в переменных окружения.

## 🛠 Стек технологий
*   **Python 3.10+**
*   **aiogram 3.13** (Асинхронный фреймворк для Telegram)
*   **Google Gemini API** (LLM с поддержкой Function Calling)
*   **python-dotenv** (Управление переменными окружения)

## 🚀 Как запустить локально

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/olgatazkorob7-png/b2b-sales-ai-bot.git
   cd b2b-sales-ai-bot
Установите зависимости:

bash
pip install -r requirements.txt
Создайте файл .env в корне проекта и добавьте ваши ключи:

env
BOT_TOKEN=ваш_токен_от_BotFather
GEMINI_API_KEY=ваш_ключ_от_Google
Запустите бота:

bash
python main.py
Примеры использования
"Дай сводку по лидам на сегодня" — бот вызывает функцию get_crm_leads() и красиво оформляет ответ.

"Напиши письмо Ивану. Он хочет скидку 10%, но сомневается в бюджете" — бот сгенерирует профессиональный текст письма.
Проект разработан в рамках портфолио Fullstack/AI-разработчик
