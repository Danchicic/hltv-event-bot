from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from Parcing_mathes import main
import datetime

bot = Bot(token='5105466929:AAEL52p3QFUbVXNDTYk-agoKyMymooShH3k')
dp = Dispatcher(bot)
today = "%d" % datetime.datetime.now().day

todayb = KeyboardButton('Матчи на сегодня')
another_event = KeyboardButton('Другой ивент')
nextb = KeyboardButton('Матчи на другие дни')

keyb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
another_games_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyb.add(todayb)
keyb.add(nextb)

keyn.add(another_event)

another_games_kb.add(another_event)
another_games_kb.add(nextb)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Привет\nПришли ссылку на ивент чтобы узнать матчи')


@dp.message_handler(text=['Матчи на сегодня'])
async def print_today_matches(msg: types.Message):
    await msg.answer('Итак, матчи на сегодня:')
    for x in main(url):
        if today == x[:2]:
            await msg.reply(x, reply_markup=another_games_kb)


@dp.message_handler(text=['Матчи на другие дни'])
async def another_games(msg: types.Message):
    for x in main(url):

        if today != x[:2]:
            await msg.reply(x, reply_markup=keyn)


@dp.message_handler(text=['Другой ивент'])
async def another_event_games(msg: types.Message):
    await msg.answer('Если хочешь посмотреть матчи на другой ивент, то пришли ссылку')


@dp.message_handler(text=['пососи'])
async def m(msg: types.Message):
    await msg.answer('Пошел на**й')


@dp.message_handler()
async def get_event_url(msg: types.Message):
    global url
    url = msg.text
    href = url.split('/')
    if "https://www.hltv.org/events/" in url:
        await msg.reply('Отлично я получил ссылку\nИнформацию о каких матчах ты хочешь получить?', reply_markup=keyb)
    else:
        await msg.answer('Неверный Ввод, попробуй еще раз')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
