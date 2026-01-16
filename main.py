from itertools import chain

from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
import asyncio
from dotenv import load_dotenv
import os
from pathlib import Path
import random

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

images_folder = Path('image_src')


def image_gen():
    photos = list(chain(images_folder.glob('*.jpg'), images_folder.glob('*.png'), images_folder.glob('*.jpeg')))
    photo = random.choice(photos)
    photo = FSInputFile(photo)
    return photo


@dp.message()
async def send_image(message: types.Message):
    print(message.text)
    chat_id = message.chat.id
    photo = image_gen()
    print(photo)
    await bot.send_photo(chat_id=chat_id, photo=photo, caption='Жопа')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
