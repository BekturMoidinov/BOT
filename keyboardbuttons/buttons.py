from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def quest_button():
    markup = InlineKeyboardMarkup(row_width=1)
    qb=InlineKeyboardButton('Quastions❔', callback_data='question_base')
    qb1 = InlineKeyboardButton('Check for bad user📛', callback_data='bad')
    qb3=InlineKeyboardButton('Registration🐧', callback_data='reg')
    qb4 = InlineKeyboardButton('Feedback💬 and Offer🫴', callback_data='fo')
    qb5=InlineKeyboardButton('My profile🦾', callback_data='mypo')
    qb6=InlineKeyboardButton('Update profile🪺', callback_data='update')
    qb7=InlineKeyboardButton('Delete my profile☠️', callback_data='delete')
    qb8=InlineKeyboardButton('View profiles🫨', callback_data='view')
    qb9=InlineKeyboardButton('Complain💢', callback_data='compl')
    markup.add(qb,qb1,qb3,qb4,qb5,qb6,qb7,qb8,qb9)
    return markup


async def question_for_transpot_type(var1,var2,var3,var4):
    markup = InlineKeyboardMarkup(row_width=1)
    air=InlineKeyboardButton(var1, callback_data='aa'+var1)
    car=InlineKeyboardButton(var2, callback_data='cc'+var2)
    bus=InlineKeyboardButton(var3, callback_data='bb'+var3)
    train=InlineKeyboardButton(var4, callback_data='tt'+var4)
    markup.add(air,car,bus,train)
    return markup


async def model_airplane(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    air1=InlineKeyboardButton(var1, callback_data='@'+','+var1+','+ex)
    air2=InlineKeyboardButton(var2, callback_data='#'+','+var2+','+ex)
    markup.add(air1,air2)
    return markup


async def model_car(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    car1=InlineKeyboardButton(var1, callback_data='$'+','+var1+','+ex)
    car2=InlineKeyboardButton(var2, callback_data='%'+','+var2+','+ex)
    markup.add(car1,car2)
    return markup


async def model_train(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    train1=InlineKeyboardButton(var1, callback_data='{'+','+var1+','+ex)
    train2=InlineKeyboardButton(var2, callback_data='^'+','+var2+','+ex)
    markup.add(train1,train2)
    return markup


async def model_bus(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    bus1=InlineKeyboardButton(var1, callback_data='/'+','+var1+','+ex)
    bus2=InlineKeyboardButton(var2,callback_data='&'+','+var2+','+ex)
    markup.add(bus1,bus2)
    return markup


async def yes_no(var1, var2,ex):
    markup = InlineKeyboardMarkup()
    yesbutton = InlineKeyboardButton(var1, callback_data='yes'+','+ex)
    nobutton = InlineKeyboardButton(var2, callback_data='no'+','+ex)
    markup.add(yesbutton, nobutton)
    return markup

async def write_all_userd_button():
    markup = InlineKeyboardMarkup()
    a=InlineKeyboardButton("warn all users⚠️",callback_data='warn')
    markup.add(a)
    return markup

async def rewrite():
    markup = InlineKeyboardMarkup()
    a=InlineKeyboardButton("Rewrite✏️",callback_data='re')
    markup.add(a)
    return markup

async def like_dislike(user):
    markup = InlineKeyboardMarkup()
    qb1=InlineKeyboardButton("Like👍",callback_data=f'Like_{user}')
    qb2=InlineKeyboardButton("Dislike👎",callback_data=f'Dislike_{user}')
    markup.add(qb1,qb2)
    return markup

async def chance_confirm(id):
    markup = InlineKeyboardMarkup()
    a=InlineKeyboardButton("Chance🍀",callback_data=f'chance_{id}')
    b=InlineKeyboardButton("Confirm😐",callback_data=f'confirm_{id}')
    markup.add(a,b)
    return markup