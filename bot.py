import telebot
from logic import Text2ImageAPI
from config import TOKEN, API_TOKEN, SECRET_KEY


bot = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
#@bot.message_handler(commands=['help', 'start'])
#def send_welcome(message):
#    bot.send_message(message, "Напиши мне текст, а я тебе картинкочкуу, о дааааа давааай делай делай")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_TOKEN, SECRET_KEY)

    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)

    images = api.check_generation(uuid)[0]

    api.save_image(images, "decoded_image.jpg")
    with open('decoded_image.jpg', 'rb') as photo:
        bot.send_photo(message.chat_id, photo)

bot.polling()