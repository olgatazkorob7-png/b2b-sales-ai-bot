import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import google.generativeai as genai

# Загружаем переменные окружения (ключи)
load_dotenv()

# --- НАСТРОЙКА GEMINI ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Создаем имитацию базы данных CRM (наши "лиды")
def get_crm_leads() -> str:
    """Возвращает список текущих лидов из CRM (имитация)"""
    return """
    Лид 1: Иван Петров, компания "Ромашка", статус: Горячий, бюджет: 150 000 руб.
    Лид 2: Анна Смирнова, компания "Вектор", статус: Теплый, бюджет: 50 000 руб. (думает)
    Лид 3: ООО "СтройМастер", статус: Холодный, бюджет: Неизвестен.
    """

# 2. Настраиваем модель и передаем ей нашу функцию (Tool Calling)
model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    tools=[get_crm_leads], 
    system_instruction="Ты — профессиональный AI-ассистент отдела продаж. Ты помогаешь менеджеру работать с лидами и писать письма."
)

# --- НАСТРОЙКА ТЕЛЕГРАМ БОТА ---
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "👋 Привет! Я твой AI-ассистент по продажам.\n\n"
        "Я умею:\n"
        "1️⃣ Доставать сводку по лидам из CRM (напиши: 'Дай сводку по лидам')\n"
        "2️⃣ Писать письма клиентам (напиши: 'Напиши письмо Ивану, он хочет скидку')\n\n"
        "Чем поможем сегодня?"
    )
    await message.answer(text)

@dp.message()
async def handle_message(message: types.Message):
    chat = model.start_chat()
    
    try:
        # Отправляем запрос в Gemini
        response = await asyncio.to_thread(chat.send_message, message.text)
        
        # Проверяем, не решил ли Gemini вызвать функцию
        for part in response.parts:
            if part.function_call:
                function_name = part.function_call.name
                
                if function_name == "get_crm_leads":
                    leads_data = get_crm_leads()
                    
                    # Отправляем данные обратно в Gemini, чтобы он красиво их оформил
                    function_response = genai.protos.Part(
                        function_response=genai.protos.FunctionResponse(
                            name=function_name,
                            response={'result': leads_data}
                        )
                    )
                    
                    final_response = await asyncio.to_thread(chat.send_message, function_response)
                    await message.answer(final_response.text)
                    return

        # Если функция не вызывалась, просто отвечаем текстом
        await message.answer(response.text)
        
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("Упс, произошла ошибка. Попробуй еще раз.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
