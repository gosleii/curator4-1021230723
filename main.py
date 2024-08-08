import telebot

bot = telebot.TeleBot('7353911403:AAGhFAyK6EJLGBEL2oQYT6C7p4jPZOfd238')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, эксперт!\n\n Тут ты можешь познакомиться с новостями. Чтобы узнать команды, пропиши *Узнать*', parse_mode='Markdown')

@bot.message_handler(commands=['Узнать'])
def main(message):
    bot.send_message(message.chat.id, 'Пока что бот в разработке, но ты можешь познакомиться с интересными трансферами или подписаться на мой [ТГК](https://t.me/DivExperted).\n\nПиши *Трансферы*', parse_mode='Markdown')

@bot.message_handler(commands=['Трансферы'])
def main(message):
    bot.send_message(message.chat.id, 'Есть громкие новости в нескольких клубах. Чтобы узнать новости в клубах, то просто напишите *название клуба*. Есть новости из Торпедо, СКА', parse_mode='Markdown')

@bot.message_handler(commands=['Торпедо'])
def main(message):
    bot.send_message(message.chat.id, '*Бум в Торпедо*\n \n В этом межсезонье в Торпедо перешли 3 игрока из АК Барса. В самом начале Дмитрий Кагарлицкий, а в конце Июля Евгений Свечников и Вячеслав Войнов. Игроки с огромным опытом. Как заявил Игорь Николавич Ларионов, что с такой историей в 78 лет у Торпедо не было титулов и в этом сезоне команда может погреметь.', parse_mode='Markdown')

@bot.message_handler(commands=['СКА'])
def main(message):
    bot.send_message(message.chat.id, '*В СКА перешёл Евгений Кузнецов*\n\n Бывший игрок Вашингтона и Каролины подписал контракт на 4 года с оплатой 50 млн в первый сезон, а в остальные три 92 млн., в честь его номера, как сообщают многие ТГ-каналы', parse_mode='Markdown')

bot.infinity_polling()