from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery

from database import ddbb
from config import bot,mediaa,admin1,admin2
from const import FirstCaption,Userinfo
from keyboardbuttons import buttons,menu_buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

async def foradmin(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id in (int(admin1),int(admin2)):
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
        if m.from_user.id in (int(admin1),int(admin2)):
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
    choice=State()
    answer=State()
async def foradmin3(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id in (int(admin1),int(admin2)):
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
            async with state.proxy() as data:
                data['id']=int(m.text)
            answer = datab.select_idea_problem_feedback_problem_table(
                tg_id=int(m.text)
            )
            await bot.send_message(
                chat_id=m.from_user.id,
                text=f'idea💡:\n'
                     f'{answer[0]}\n'
                     f'problem📛:\n'
                     f'{answer[1]}',
                reply_markup=await buttons.answer_go_back()
            )
            await see_idea_problem.next()
        elif int(m.text) not in idss:
            await bot.send_message(
                chat_id=m.from_user.id, text='There is no such kind of user id.\n'
            )
            await state.finish()
    elif m.text.lower()=='stop':
        await bot.send_message(
            chat_id=m.from_user.id, text='Bye!'
        )
        await state.finish()
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text='write "stop correctly!"'
        )


async def choice_answer(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Write answer to that user.'
    )
    await see_idea_problem.next()

async def choice_go_back(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await see_idea_problem.previous()

async def load_answer(m:types.Message,state:FSMContext):
    datab=ddbb.Database()
    await bot.send_message(
        chat_id=m.from_user.id,
        text='Ur answer was succesfully sent🎉🎊.'
    )
    async with state.proxy() as data:
        datab.insert_admin_rating(
            admin=m.from_user.id,
            tg_id=data['id']
        )
        datab.delete_feedb_probl_table(
            tg=data['id']
        )
        await bot.send_message(
            chat_id=data['id'],
            text=f'Hi,this is the answer from admin🎅:\n'
                 f'{m.text.capitalize()}'
        )
        await bot.send_message(
            chat_id=data['id'],
            text='U can rate message 🧑‍🌾 or skip it 🏂.',
            reply_markup= await buttons.skip_rate()
        )
    await state.finish()


class Rate(StatesGroup):
    rate=State()

async def start_rating(call:types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Rate it from 1 to 5'
    )
    await Rate.rate.set()
async def load_rating(m:types.Message,state:FSMContext):
    datab=ddbb.Database()
    if m.text.isdigit():
        if 0<int(m.text)<=5:
            datab.update_admin_rating_rating(
                rating=int(m.text),
                tg_id=m.from_user.id
            )
            await bot.send_message(
                chat_id=m.from_user.id,
                text='Thank you for your attention'
            )
            await state.finish()
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='Please rate between 1 and 5 💢 .'
            )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text='Please write only digits💢.'
        )

async def skip(call:types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Okay👍'
    )


async def foradmin4(m:types.Message):
    datab=ddbb.Database()
    if m.from_user.id in (int(admin1),int(admin2)):
        rating1=[i[0] for i in datab.select_admin_rating_table(tg_id=int(admin1))]
        rating2=[i[0] for i in datab.select_admin_rating_table(tg_id=int(admin2))]
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'Bektur:{rating1}\n'
                 f'Adilet:{rating2}'
        )
        if len(rating1):
            ave1=round(sum(rating1)/len(rating1),0)
        else:
            ave1=0
        if len(rating2):
            ave2 = round(sum(rating2) / len(rating2), 0)
        else:
            ave2=0
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'Average ratings:\n'
                 f'bektur: {ave1}\n'
                 f'adilet: {ave2}'
        )


def register_admin(dp:Dispatcher):
    dp.register_message_handler(foradmin, commands="check_users")
    dp.register_message_handler(foradmin2, commands="user_answers")
    dp.register_message_handler(foradmin3, commands="feedback_and_problem")
    dp.register_message_handler(load_id, state=see_idea_problem.id,content_types=['text'])
    dp.register_callback_query_handler(choice_go_back,lambda call:call.data=='go',state=see_idea_problem.choice)
    dp.register_callback_query_handler(choice_answer,lambda call:call.data=='ans',state=see_idea_problem.choice)
    dp.register_message_handler(load_answer,state=see_idea_problem.answer,content_types=['text'])
    dp.register_callback_query_handler(start_rating,lambda call:call.data=='rate')
    dp.register_callback_query_handler(skip,lambda call:call.data=='skip')
    dp.register_message_handler(load_rating,state=Rate.rate,content_types=['text'])
    dp.register_message_handler(foradmin4,commands='see_admins_rating')