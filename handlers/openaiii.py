# import g4f
# import nest_asyncio
# from aiogram import types, Dispatcher
# from config import bot,admin1,admin2
# from keyboardbuttons import buttons
# from database import ddbb
# from aiogram.utils.deep_linking import _create_link
# import os
# import binascii
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
#
#
# nest_asyncio.apply()
# def request(text):
#     g4f.debug.logging = True
#     g4f.debug.version_check = False
#     response = g4f.ChatCompletion.create(
#         model=g4f.models.gpt_4,
#         messages=[{"role": "user", "content": text}],
#     )
#     return response.encode('utf-8')
#
# class AI(StatesGroup):
#     text = State()
#
# async def start(call: types.CallbackQuery):
#     await bot.send_message(
#         call.from_user.id,
#         text='U have been connected with AI\n'
#              'If u want to finish write "stop"'
#     )
#     await AI.text.set()
#
# async def load_request(m: types.Message, state: FSMContext):
#     if m.text.lower() != 'stop':
#         await bot.send_message(
#             chat_id=m.from_user.id,
#             text=request(m.text)
#         )
#     else:
#         await state.finish()
#
#
# def register_openai(dp:Dispatcher):
#     dp.register_callback_query_handler(start,lambda call:call.data=='ai')
#     dp.register_message_handler(load_request,state=AI.text,content_types=['text'])
#
