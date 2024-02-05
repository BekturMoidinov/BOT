from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
memory=MemoryStorage()
token=config('TOKEN')
mediaa=config('MEDIA')
admin1=config('ADMIN1_ID')
admin2=config('ADMIN2_ID')
chat1_id=config('CHAT1_ID')
bot=Bot(token=token,proxy=PROXY_URL)
dp=Dispatcher(bot=bot, storage=memory)