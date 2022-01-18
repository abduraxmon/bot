import logging
import wikipedia
import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/65fdd0ea3da92da45fe8e6f3/latest/uzs'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5016520118:AAE5PwOMpMRkNXmjnqAX71XaKCJaRDekQ6o'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum. My Wiki Botga Xush kelibsz! Bu yerda siz istalgan ma'lumotingizni qidirsangiz bo'ladi Googlega o'xshab. MyWiki Bot Asoschisi Ashurov Abduraxmon! @al_djami")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
          respond=wikipedia.summary(message.text)
          await message.answer(respond)
    except:
        await message.reply("Kechirasz, bu mavzuga oid maqola topilmadi!☹")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)