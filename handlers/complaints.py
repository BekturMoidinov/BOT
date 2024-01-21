from tkinter import Image
import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import Update
from random import choice
from database import ddbb
from config import bot,mediaa
from const import FirstCaption,Userinfo
from keyboardbuttons import buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class Complaints(StatesGroup):
    who=State()

async def get_complaints(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Who annoys u (write person`s first name)'
    )
    await Complaints.who.set()
async def load_name(m: types.Message, state: FSMContext):
    data=ddbb.Database()
    rows=data.select_user()
    ids=[i[0] for i in rows]
    names=[i[1] for i in rows]
    if m.text in names:
        await bot.send_message(
            chat_id=m.from_user.id,
            text='Thank u for informing.We will panish that person'
        )
        await bot.send_message(
            chat_id=ids[names.index(m.text)],
            text=f'Hi {m.text}\n'
                 f'there was a complaint about you\n'
        )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text='There is no such kind of person'
        )
    await state.finish()

def register_complaints(dp: Dispatcher):
    dp.register_callback_query_handler(get_complaints,lambda call:call.data=='compl')
    dp.register_message_handler(load_name,state=Complaints.who,content_types=['text'])