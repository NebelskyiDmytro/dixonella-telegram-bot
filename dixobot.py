import logging

from steam_community_market import Market, AppID
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN_API

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

market = Market("UAH")

sticker = "Sticker | Natus Vincere (Gold) | Paris 2023"
awp = "AWP | Chromatic Aberration (Minimal Wear)"

menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Get Sticker Price'),
    KeyboardButton('Get AWP Price')
)

async def send_stickerprice(message: types.Message):
    await message.answer((sticker + ": "+ str(market.get_lowest_price(sticker, AppID.CSGO)) + " UAH"))
    await message.delete()

async def send_awpprice(message: types.Message):
    await message.answer((awp + ": " + str(market.get_lowest_price(awp, AppID.CSGO)) + " UAH"))
    await message.delete()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hey there ! I am d1xonella bot. This is Beta.v")

@dp.message_handler(content_types=['text'])
async def process_message(message: types.Message):
    # Если пользователь нажал на кнопку "Стоимость стикера"
    if message.text == 'Get Sticker Price':
        await send_stickerprice(message)
    # Если пользователь нажал на кнопку "Стоимость AWP"
    elif message.text == 'Get AWP Price':
        await send_awpprice(message)
    # Если пользователь отправил другое сообщение, отправляем ему меню
    else:
        await message.answer('Select what do you want to get:', reply_markup=menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
