from aiogram import types, Dispatcher
from config import bot,admin
from keyboardbuttons import buttons
from database import ddbb
from aiogram.utils.deep_linking import _create_link
import os
import binascii

async def reference_menu(call: types.CallbackQuery):
    datab=ddbb.Database()
    info=datab.select_balance_totalreferral_table(tg_id=call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f'Welcome to referral menu\n'
             f'Share me and invite others\n'
             f'to earn money🤑!!\n'
             f'Balance: {info[0]}\n'
             f'Referrals: {info[1]}\n'
             f'Press button below to generate link',
        reply_markup= await buttons.generate_link()
    )


async def generate_link(call: types.CallbackQuery):
    datab=ddbb.Database()
    link_user=datab.select_all_from_tl_users(tg_id=call.from_user.id)[5]
    if link_user:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'Your old link: {link_user}'
        )
    else:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        datab.update_tg_user_link(link=link,tg_id=call.from_user.id)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'Your new link: {link}'
        )
async def see_referrals(call: types.CallbackQuery):
    datab=ddbb.Database()
    referrals=datab.select_referrals_referral_table(tg_id=call.from_user.id)
    ids=[i[0] for i in referrals]
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f'Your referrals: {ids}'
    )
async def balance(call: types.CallbackQuery):
    datab=ddbb.Database()
    balance=datab.select_all_from_tl_users(tg_id=call.from_user.id)[6]
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f'Your balance: {balance}'
    )
def register_referrence(dp:Dispatcher):
    dp.register_callback_query_handler(reference_menu,lambda call:call.data=='ferral')
    dp.register_callback_query_handler(generate_link,lambda call:call.data=='generate_link')
    dp.register_callback_query_handler(see_referrals,lambda call:call.data=='jjj')
    dp.register_callback_query_handler(balance,lambda call:call.data=='balance')