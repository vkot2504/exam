import schedule 
import telebot
from time import sleep
from threading import Thread






TOKEN = '6025323622:AAHAWeqAHWmiSUflt-0Od0C5s1jhodMNMO4'
bot = telebot.TeleBot(TOKEN)
some_id = 435005825

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(some_id, 'Вот уже и утро наступило! Не правда ли?! Пора выбрать котика, умоляющего поставить мне пятерочку за экзамен. Жду в ответ цифру от 0 до 5. P.S. интереснее присылать цифры по порядку. Но Вы просили пользователю дать возможность выбрать котиков. Дополнение- если Вы читаете это дополнение, значит мне все-таки удалось соединиться с часовым поясом сервера, чему я безумно рад сам! Если бы я знал, что столкнусь с такой проблемой -сделал бы еще котика про конкретy ситуацию с часовым поясом. UPD в очередной раз что-то пошло не так, я исправил ситуацию с ID. И если вы читаете уже это сообщение- то у меня все получилось') 

if __name__ == "__main__":
    schedule.every().day.at("08:30").do(function_to_run)
    Thread(target=schedule_checker).start() 




@bot.message_handler(content_types=['text'])
def text(message):
    chatId=message.chat.id
    text= message.text.lower ()
    print (text)
    if text == 'start':
        bot.send_message(message.chat.id, 'Доброго времени суток, Карим Аммарович! Вы попали в бот Вашего студента- Межанова Василия. Каждый день в определенное время (я выставил 9 часов утра) бот будет спрашивать у Вас, какого котика Вы хотите увидеть сегодня. Котиков я сделал не так много, все же тут актуальнее именно механизм бота. P.S. Фотография котика на аватарке бота взята из открытого источника.')
    elif text == '1':
        p= open('1.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '2':
        p= open('2.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '3':
        p= open('3.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '4':
        p= open('4.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '5':
        p= open('5.png', 'rb')
        bot.send_photo(message.chat.id,p)


bot.polling()
    
    

