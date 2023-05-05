import logging

from steam_community_market import Market, AppID
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6089352897:AAFJC_LSB7jhF1MO9-Xu24J576-wSJtW7VQ')
dp = Dispatcher(bot)

market = Market("UAH")

sticker = "Sticker | Natus Vincere (Gold) | Paris 2023"
awp = "AWP | Chromatic Aberration (Minimal Wear)"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hey there ! I am d1xonella bot. This is Beta.v")

@dp.message_handler(commands=['stickerprice'])
async def send_help(message: types.Message):
    await message.reply(sticker, ": " + market.get_lowest_price(sticker, AppID.CSGO), "UAH")

@dp.message_handler(commands=['awpprice'])
async def send_help(message: types.Message):
    await message.reply(awp, ":" + market.get_lowest_price(awp, AppID.CSGO), "UAH")

# хэндлер на любое сообщение
@dp.message_handler()
async def echo(message: types.Message):
    """
    Этот хэндлер будет вызываться на любое сообщение от пользователя.
    Он будет отвечать на сообщение, повторяя его текст.
    """
    await message.reply(message.text)

# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
