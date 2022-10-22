from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message, CallbackQuery, LabeledPrice
from dotenv import load_dotenv
from keyboards import *
from work import *
import os

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)



executor.start_polling(dp)







