from aiogram import executor, Dispatcher, Bot
from handlers import start,qustions,group_filter,for_admin,registration
from config import dp
from database import ddbb
async def on_startup(_):
    data=ddbb.Database()
    data.create_table()
start.register_start_handler(dp=dp)
qustions.register_ask(dp=dp)
registration.registr_reg_handler(dp=dp)
for_admin.register_admin(dp=dp)
group_filter.register_group_filter(dp=dp)
if __name__ == '__main__':
    executor.start_polling(
        dp, skip_updates=True,
        on_startup=on_startup
    )