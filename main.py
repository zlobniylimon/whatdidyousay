from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import voicetotext

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['voice'])
async def voice_to_text(message: types.Message):
    await message.voice.download('voice.oga')
    await message.answer(f'voice is downloaded')
    data = voicetotext.convert_voicetotext('voice.oga')
    await message.reply(data)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
