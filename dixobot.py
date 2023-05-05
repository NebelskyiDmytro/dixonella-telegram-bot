import logging

from steam_community_market import Market, AppID
from aiogram import Bot, Dispatcher, executor, types

# установить уровень логирования
logging.basicConfig(level=logging.INFO)

# инициализировать бота и диспетчер
bot = Bot(token='6089352897:AAFJC_LSB7jhF1MO9-Xu24J576-wSJtW7VQ')
dp = Dispatcher(bot)

market = Market("UAH")

item = "AWP | Chromatic Aberration (Field-Tested)"

# хэндлер на команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Этот хэндлер будет вызываться, когда пользователь введет команду /start.
    Он отправит приветственное сообщение с инструкциями.
    """
    await message.reply("Hey there ! I am d1xonella bot. This is Beta.v")

# хэндлер на команду /help
@dp.message_handler(commands=['price'])
async def send_help(message: types.Message):
    await message.reply(market.get_lowest_price(item, AppID.CSGO))

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
