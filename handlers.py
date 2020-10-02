from loader import dp
from aiogram.dispatcher.filters import Command
from keybaord import menu
from scrap import parse

@dp.message_handler(Command('start'))
async def reply(message):
    await message.answer('Добро пожаловать !', reply_markup = menu)

@dp.message_handler(text = 'Parse')
async def answr(message):
    await message.answer(parse())


