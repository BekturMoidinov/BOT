from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery

from database import ddbb
from config import bot,mediaa,admin
from const import FirstCaption,Userinfo
from keyboardbuttons import buttons,menu_buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

async def foradmin(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id == int(admin):
            await bot.send_message(
                chat_id=m.from_user.id,
                text=f'Welcome to Admins menu {m.from_user.first_name}!',
                reply_markup=await menu_buttons.menu_buttons_for_admin("See all users📃", "See all bad users👿")
            )
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='It is only for admin'
            )

async def foradmin2(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id == int(admin):
            await bot.send_message(
                chat_id=m.from_user.id,
                text=f'Welcome to Admins menu {m.from_user.first_name}!',
                reply_markup=await menu_buttons.menu_buttons_for_admin2("See all users answer🙈")
            )
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='It is only for admin'
            )
class see_idea_problem(StatesGroup):
    id=State()
async def foradmin3(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id == int(admin):
            datab=ddbb.Database()
            ids=datab.select_id_feedback_problem_table()
            idss=[i[0] for i in ids]
            if ids:
                await bot.send_message(
                    chat_id=m.from_user.id,
                    text=f'Here are the user`s id who has feedback and problems\n'
                         f'{idss}'
                )
                await bot.send_message(
                    chat_id=m.from_user.id,
                    text='Write down one id in order to see what this user has written👇\n'
                         "To stop 🫸 write 'stop'"
                )
                await see_idea_problem.id.set()
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='It is only for admin'
            )

async def load_id(m:types.Message,state:FSMContext):
    datab=ddbb.Database()
    ids=datab.select_id_feedback_problem_table()
    idss=[i[0] for i in ids]
    if m.text.isdigit():
        if int(m.text) in idss:
            answer = datab.select_idea_problem_feedback_problem_table(
                tg_id=int(m.text)
            )
            await bot.send_message(
                chat_id=m.from_user.id,
                text=f'idea💡:\n'
                     f'{answer[0]}\n'
                     f'problem📛:\n'
                     f'{answer[1]}'
            )
        elif int(m.text) not in idss:
            await bot.send_message(
                chat_id=m.from_user.id, text='There is no such kind of user id.Try again🫡\n'
                                             "To stop 🫸 write 'stop'"
            )
    else:
        if m.text=='stop':
            await bot.send_message(
                chat_id=m.from_user.id,
                text='Okay👌'
            )
            await state.finish()
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='If u want to stop\n'
                     'write "stop" correctly!'
            )
def register_admin(dp:Dispatcher):
    dp.register_message_handler(foradmin, commands="check_users")
    dp.register_message_handler(foradmin2, commands="user_answers")
    dp.register_message_handler(foradmin3, commands="feedback_and_problem")
    dp.register_message_handler(load_id, state=see_idea_problem.id,content_types=['text'])