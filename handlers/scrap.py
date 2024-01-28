from aiogram import types, Dispatcher
from config import bot,admin
from keyboardbuttons import buttons
from database import ddbb
from aiogram.utils.deep_linking import _create_link
import os
import binascii
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from scrapping.english_scrapper import EnglishScrapper

async def english_adv(call: types.CallbackQuery):
    datab=ddbb.Database()
    scrapper = EnglishScrapper()
    links=scrapper.parse_data()
    for link in links[:5]:
        datab.insert_eng_table(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link,reply_markup=await buttons.save(link))


async def eng_favourite(call: types.CallbackQuery):
    await call.message.delete()
    datab=ddbb.Database()
    datab.insert_favo_eng_table(
        tg_id=call.from_user.id,
        link=call.data[5:]
    )

def register_scrap(dp: Dispatcher):
    dp.register_callback_query_handler(english_adv, lambda call:call.data=='advanced')
    dp.register_callback_query_handler(eng_favourite, lambda call:call.data.startswith('save'))