from aiogram import types, Dispatcher
from config import bot
from keyboardbuttons import buttons
from database import ddbb
async def ask(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Type of transport u prefer:",
        reply_markup= await buttons.question_for_transpot_type('Air','Car','Train','Bus')
    )

async def answer_airmodel(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich plane do like most:",
        reply_markup= await buttons.model_airplane('Boeing','Airbus',call.data.replace('aa',''))
    )
async def answer_carmodel(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich car do like most:",
        reply_markup= await buttons.model_car('BMW','Mercedes',call.data.replace('cc',''))
    )
async def answer_Busmodel(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich bus do like most:",
        reply_markup= await buttons.model_bus('London Routemaster (London Bus)','Mercedes-Benz Citaro (Various Cities Worldwide)',call.data.replace('bb',''))
    )
async def answer_trainmodel(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich train do like most:",
        reply_markup= await buttons.model_train('Shinkansen (Bullet Train) - Japan','TGV (Train à Grande Vitesse) - France',call.data.replace('tt',''))
    )
async def yesno_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Have u ever been on it:",
        reply_markup=await buttons.yes_no("yes","no",call.data[2:])
    )
async def thanks(call: types.CallbackQuery):
    gg=call.data.split(',')
    database=ddbb.Database()
    database.create_table_answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Thank you for answering"
    )
    database.insert_answer(
        telegram_id=call.from_user.id,
        type=gg[2],
        model=gg[1],
        exp=gg[0]
    )
t=[str(i) for i in range(1,9)]
h=set(t)
def register_ask(dp: Dispatcher):
    dp.register_callback_query_handler(ask, lambda call: call.data == "question_base")
    dp.register_callback_query_handler(answer_airmodel, lambda call:call.data.startswith("aa"))
    dp.register_callback_query_handler(answer_carmodel, lambda call:call.data.startswith("cc"))
    dp.register_callback_query_handler(answer_trainmodel, lambda call:call.data.startswith("tt"))
    dp.register_callback_query_handler(answer_Busmodel, lambda call:call.data.startswith("bb"))
    dp.register_callback_query_handler(yesno_answer, lambda call:bool(len(set(call.data).intersection(h))))
    dp.register_callback_query_handler(thanks, lambda call:call.data.startswith("yes"))
    dp.register_callback_query_handler(thanks, lambda call:call.data.startswith("no"))