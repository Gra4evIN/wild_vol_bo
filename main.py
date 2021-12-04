import telebot
from extensions import APIException, Convertor
from config import TOKEN, exchanges
import traceback
import emoji


TOKEN = "1910659318:AAGR_An5s5rNuesQaYnfYmhBQB2yJrJe8kg"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Прием заявок на 2022 год начинается с 05.12.2021 года.\nОсновные команды для помощи: \n/help \n /faq \n/time_to_work \n /stuff \n /communication \n /vaccination \n /food \n /accomodation"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['faq'])
def faq(message: telebot.types.Message):
    text = "Для прохождении волонтерских работ на территории Кроноцкого государственного заповедника/Южно-Камчатского федерального заказника, для постановки в график необходимо:\n1) Заполнить анкету на прохождение обучения в Школе Защитников Природы, ссылка на форму анкеты:https://docs.google.com/forms/d/1idhdo4KswngdMijyXZWx_TXGWqJuKn7ySRzjeR0UnsI/edit\n\2) Пройти курс, по окончании которого у Вас будет итоговый тест, в случае успешного результата Вас перенаправят в отдел познавательного туризма, далее Вы заполняете еще одну анкету (волонтера Кроноцкого заповедника) по утвержденной форме на сайте www.kronoki.ru, в разделе ВОЛОНТЕРСТВО, в левом меню выбираем пункт ОФОРМИТЬ ЗАЯВКУ."
    bot.reply_to(message, text)

@bot.message_handler(commands=['time_to_work'])
def time_to_work(message: telebot.types.Message):
    text = "Минимальный срок работы на охраняемых территориях-3 недели."
    bot.reply_to(message, text)

@bot.message_handler(commands=['stuff'])
def stuff(message: telebot.types.Message):
    text = "Потребуется стандартное походное снаряжение, за исключением палатки и посуды для приготовления еды на костре: высокие резиновые сапоги («болотники»), спальник, коврик, налобный фонарик, термос, личная посуда, биоразлагаемые средства гигиены, репелленты.\nПогода на Камчатке быстро и часто меняется – не забудьте про теплую и водоотталкивающую одежду и обувь.\nВ теплые дни из соображений этики нельзя ходить по кордону в купальнике и коротких шортах,поэтому комплект легкой одежды тоже возьмите с собой. \nПомните, вы – лицо заповедника, наравне с сотрудниками!"
    bot.reply_to(message, text)


@bot.message_handler(commands=['communication'])
def communication(message: telebot.types.Message):
    text = "\rНа всех кордонах есть возможность зарядить гаджеты, однако сотовой связи нигде нет. \vНа кордонах есть интернет по вечерам, но очень медленный "
    bot.reply_to(message, text)


@bot.message_handler(commands=['vaccination'])
def vaccination(message: telebot.types.Message):
    text = "Заповедные территории – зоны высокой вулканической и сейсмической активности, вокруг множество диких животных, а штатных врачей на кордонах нет. Поэтому мы приветствуем медицинские справки, а также просим вас самостоятельно оформить страхование жизни и здоровья, также необходимо иметь при себе отрицательный ПЦР тест на Covid-19.Не забудьте взять личную аптечку! "
    bot.reply_to(message, text)

@bot.message_handler(commands=['food'])
def food(message: telebot.types.Message):
    text = "Основные продукты питания предоставляютя волонтеру. Заповедник обеспечивает пайком каждого волонтера." \
           "Вам необходимо будет только докупить для себя фрукты,овощи, кондитерские изделия, молочные продукты" \
            "по своему вкусовому предпочтению"
    bot.reply_to(message, text)

@bot.message_handler(commands=['accomodation'])
def accomodation(message: telebot.types.Message):
    text = "Волонтёры, работающие на кордонах, размещаются в домиках или модулях (сборные сезонные конструкции)," \
           "спят в спальниках, либо на раскладушках с постельным бельём. Туалеты расположены вне домиков. Есть баня и\или душ, " \
           "возможность стирать и сушить личные вещи. Волонтёры, участвующие в работах по прочистке троп, иногда ночуют в " \
           "палатках или в инспекторских домах на полевых стационарах (условия минимальные)."
    bot.reply_to(message, text)


bot.polling()
