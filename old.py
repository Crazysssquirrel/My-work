import random

import os

import telebot
from telebot import types

bot = telebot.TeleBot('5443833588:AAHi_nH_wLFsGOpINgJvWPEqvEA0siNInKk')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Выбрать упражнение (разгрузка)')
    btn2 = types.KeyboardButton('Что-то беспокоит')
    btn3 = types.KeyboardButton('Музыка для расслабления')
    markup.add(btn1, btn2, btn3)
    mess = f'Рад вас видеть, <b>{message.from_user.first_name}</b>. Вы ощущаете усталость или может быть вас что-то беспокоит? Хотите эффективно поработать или расслабиться?'
    bot.send_message(message.chat.id, mess,
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Выбрать упражнение (разгрузка)":
        ChooseRelaxExercise(message)
    elif message.text == "Нет, выбрать другое упражнение":
        ChooseRelaxExercise(message)
    elif message.text == 'Приступить к дыхательной практике':
        ChooseRelaxExercise(message)
    elif message.text == "Расслабление через напряжение (6 мин)":
        bot.send_message(message.chat.id,
                         "Практика направлена на то, чтобы через физическое напряжение и расслабление добиться расслабления нашего ума. Рекомендуется пойти в отдалённое, тихое место и занять удобную позу.")
        ExRelaxAudio1 = open('/opt/ReformYSbot/Exercises/Расслабление через напряжение.mp3', 'rb')
        bot.send_audio(message.chat.id, ExRelaxAudio1)
        Done(message)
    elif message.text == "Дыхание квадрат (4 мин)":
        bot.send_message(message.chat.id,
                         "Вдох, выдох и пауза примерно равны друг другу по длительности, комфортный ритм – примерно 4 секунд")
        Photo = open('/opt/ReformYSbot/Exercises/Квадрат дыхания.png', 'rb')
        bot.send_photo(message.chat.id, Photo)
        ExRelaxAudio2 = open('/opt/ReformYSbot/Exercises/Дыхание квадрат.mp3', 'rb')
        bot.send_audio(message.chat.id, ExRelaxAudio2)
        Done(message)
    elif message.text == "Асимметричное дыхание (2 мин)":
        bot.send_message(message.chat.id,
                         "Вдыхать нужно через нос, а выдыхать через рот  делать выдох в 5 раз длиннее вдоха (рекомендуется 2 секунд вдох, 10 секунд выдох")
        ExRelaxAudio3 = open('/opt/ReformYSbot/Exercises/Асимметричное дыхание.mp3', 'rb')
        bot.send_audio(message.chat.id, ExRelaxAudio3)
        Done(message)

    elif message.text == "Выполнено":
        ChooseVisualExercise(message)
    elif message.text == "Яблоневый сад (4 мин)":
        bot.send_message(message.chat.id,
                         "Рекомендуется занять удобную позу сидя и расслабиться, если есть возможность лечь на коврик на спину в позу морской звезды")
        ExVisualAudio1 = open('/opt/ReformYSbot/Exercises/Яблоневый сад.mp3', 'rb')
        bot.send_audio(message.chat.id, ExVisualAudio1)
        Done2(message)
    elif message.text == "Полёт к звезде (7 мин)":
        bot.send_message(message.chat.id,
                         "Рекомендуется занять удобную позу сидя и расслабиться, если есть возможность лечь на коврик на спину в позу морской звезды")
        ExVisualAudio2 = open('/opt/ReformYSbot/Exercises/Полёт к звезде.mp3', 'rb')
        bot.send_audio(message.chat.id, ExVisualAudio2)
        Done2(message)
    elif message.text == "Путешествие на воздушном шаре (5 мин)":
        bot.send_message(message.chat.id,
                         "Рекомендуется занять удобную позу сидя и расслабиться, если есть возможность лечь на коврик на спину в позу морской звезды")
        ExVisualAudio3 = open('/opt/ReformYSbot/Exercises/Путешествие на воздушном шаре.mp3', 'rb')
        bot.send_audio(message.chat.id, ExVisualAudio3)
        Done2(message)

    elif message.text == "Готово":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        exr1 = types.KeyboardButton('Да, помогло разгрузиться')
        exr2 = types.KeyboardButton('Нет, выбрать другое упражнение')
        exr3 = types.KeyboardButton('')
        markup.add(exr1, exr2, exr3)
        bot.send_message(message.chat.id,
                         text="Помогли ли вам упражнения?",
                         reply_markup=markup)
    elif message.text == "Да, помогло разгрузиться":
        Back(message)
    elif message.text == "Нет, выбрать другое упражнение":
        func(message)

    elif message.text == "Что-то беспокоит":
        Worry(message)
    elif message.text == 'Раздражение':
        Irritation(message)
    elif message.text == 'Упадок сил':
        Prostration(message)
    elif message.text == 'Тревога':
        Anxiety(message)


    elif message.text == 'Хочу поговорить об этом со специалистом':
        Specialist(message)

    elif message.text == 'Московский политех':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         'Вы можете записаться на консультацию со специалистом Московского политехнического университета в группе: https://vk.com/app6013442_-152977101?form_id=1#form_id=1',
                         reply_markup=markup)

    elif message.text == 'МГУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         'Вы можете записаться на консультацию со специалистом Московского государственного университета на сайте: http://www.psy.msu.ru/about/psy_help/',
                         reply_markup=markup)

    elif message.text == 'ГУУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         'Вы можете записаться на консультацию со специалистом Государственного университета управления на сайте: https://guu.ru/news_ru/91299/',
                         reply_markup=markup)

    elif message.text == 'АГУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         'Вы можете записаться на консультацию со специалистом Астраханского государственного университета на сайте: https://asu.edu.ru/studentam/10509-studencheskaia-psihologicheskaia-slujba.html',
                         reply_markup=markup)

    elif message.text == 'Музыка для расслабления':
        Music(message)
    elif message.text == 'Другая композиция':
        Music(message)

    elif message.text == "Вернуться в меню":
        Back(message)
    else:
        bot.send_message(message.chat.id,
                         text="К сожалению я пока не знаю, что на это ответить. Пожалуйста, выберите что-то из списка или нажмите /start, чтобы перейти в меню")


def ChooseRelaxExercise(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    exr1 = types.KeyboardButton('Расслабление через напряжение (6 мин)')
    exr2 = types.KeyboardButton('Дыхание квадрат (4 мин)')
    exr3 = types.KeyboardButton('Асимметричное дыхание (2 мин)')
    markup.add(exr1, exr2, exr3)
    bot.send_message(message.chat.id,
                     text="Предлагаем вам сделать упражнение, направленное на расслабление нервной системы. Выбери понравившееся",
                     reply_markup=markup)


def Done(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton('Выполнено')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите "Выполнено" после того, как завершите упражнение',
                     reply_markup=markup)


def ChooseVisualExercise(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    exr1 = types.KeyboardButton('Яблоневый сад (4 мин)')
    exr2 = types.KeyboardButton('Полёт к звезде (7 мин)')
    exr3 = types.KeyboardButton('Путешествие на воздушном шаре (5 мин)')
    markup.add(exr1, exr2, exr3)
    bot.send_message(message.chat.id,
                     text="Теперь предлагаем вам сделать небольшую медитативную практику, которая поможет снять усталость и перезагрузиться.",
                     reply_markup=markup)


def Done2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton('Готово')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите "Готово" после того, как завершите упражнение',
                     reply_markup=markup)


def Worry(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Раздражение')
    btn2 = types.KeyboardButton('Упадок сил')
    btn3 = types.KeyboardButton('Тревога')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Как вы себя чувствуете?',
                     parse_mode='html',
                     reply_markup=markup)


def Irritation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Приступить к дыхательной практике')
    btn2 = types.KeyboardButton('Вернуться в меню')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     'Испытывать раздражение и агрессию — нормальная человеческая реакция. Важно давать ему выход, но так, чтобы это не было разрушительно для вас и для других. Нужно пытаться не избавиться от агрессии, а найти возможности реализовать ее. Лучший способ реализовать свою агрессию заключается в том, чтобы чаще задавать себе вопросы «чего я хочу сейчас?» и «в чем я нуждаюсь?» и предпринимать необходимые действия для достижения этого. '
                     '\n\nУспокоиться будет гораздо проще, если вы постараетесь нейтрализовать себя не на пике гнева, а когда только почувствуете первые признаки приступа агрессии.'
                     '\nЛучше всего помогает бороться с приступами гнева спорт. Если вы уже ходите в зал, делайте это в три раза чаще. Например, по утрам, чтобы приступать к работе, уже выплеснув эмоции.'
                     '\n\nПопробуйте прямо говорить с окружающими о своем состоянии. Близкие и любимые люди, друзья, коллеги могут не догадываться, что вам не хватает их внимания, вы чувствуете себя обиженной и забытой.'
                     '\nРешившись на разговор, постарайтесь обойтись без обвинений и критики. Возможно, сначала потребуется применить один из предыдущих методов или даже испробовать их все. Лучше всего использовать «Я-сообщения» — говорить о своих ощущениях от первого лица. Тогда вы сможете спокойно объяснить, что вас задело или разозлило. Попросите собеседника объяснить его позицию — вероятно, вместе вы сможете разобраться в ситуации и найти решение.'
                     '\n\nПсихологи считают, что полезно выразить злость и обиду на бумаге или в компьютерном файле — это еще один способ выплеснуть то, что накопилось внутри. Попробуйте написать письмо тому, кто вас разозлил или обидел. Не нужно сосредотачиваться на том, чтобы написать связный, красивый текст: пишите все, что думаете и чувствуете. Потом файл можно удалить, а бумажное письмо — разорвать или сжечь. Либо, если захочется, отредактировать текст и отправить адресату.'
                     '\n\nТакже важно знать, почему возникло такое состояние и что может за этим стоять? Если Вы чувствуете, что раздражительность становится системой, не исключением, а правилом, повышенный тон разговора входит в привычку — это сигнал, что надо серьезно подойти к решению проблемы и восстановить гармонию вашего внутреннего мира, иначе это пойдет Вам во вред.'
                     '\nРазобравшись с возможными причинами раздражительности, обратимся ко второму вопросу: как все же управлять своей реакцией и не раздражаться?'
                     '\n\n1. Изучите свои триггеры — те ситуации, которые вызывают у Вас раздражение. Составьте список: 5-10 основных источников раздражения. На самом деле их больше, если расписать подробнее по разным сферам жизни. Например, в транспорте меня раздражает одно, на работе другое, в отношениях — третье. Далее, проследите историю каждого триггера: почему Вас это раздражает. Это очень действенный способ.'
                     '\n2. Узнайте больше про механизм раздражения, прочитайте об этом. Знание о том, как устроены наши эмоции, очень помогает — мы начинаем понимать их биологические и психологические мотивы.'
                     '\n3. Старайтесь уловить момент, когда раздражение только начинает зарождаться в Вас, — тогда будет проще прервать контакт с объектом, переадресовать эмоцию или применить другую тактику — например, глубоко дышать.'
                     '\n4. Избегайте ситуаций, где срабатывают ваши триггеры. Легко сказать и трудно сделать, но попробуйте составить маршрут в объезд пробок или просто поменяйте подход к тому, что вызывает раздражение.',
                     parse_mode='html',
                     reply_markup=markup)


def Prostration(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Хочу поговорить об этом со специалистом')
    btn2 = types.KeyboardButton('Вернуться в меню')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     'Чтобы понять, почему ваше отношение к работе изменилось в худшую сторону, нужно проанализировать свои ожидания, надежды и планы, связанные с профессиональной деятельностью. Вероятно, некоторые из них, причем, важные для вас, оказались нереализованными. Если это на самом деле так, то подумайте, можете ли вы изменить ситуацию, оставаясь на прежнем месте работы. Можете? значит, задумываться о переходе ещё рано. '
                     '\n\nЕсли копнуть ещё глубже, то стоит задуматься о том, почему, исходя из каких соображений вы выбрали эту работу. Было ли это ваше собственное решение или оно совершалось под влиянием мнения других людей? Выбор был сделан кем-то за вас? пора брать жизнь в - свои руки.'
                     '\n\nНаконец, нужно подумать и о том, соответствует ли ваш характер, ваши индивидуальные особенности и черты той работе, которую вы делаете, тем требованиям, которые она предъявляет. Рассогласования и несовпадения могут оказаться подлинными причинами эмоционального выгорания.',
                     parse_mode='html',
                     reply_markup=markup)


def Anxiety(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Хочу поговорить об этом со специалистом')
    btn2 = types.KeyboardButton('Вернуться в меню')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     'Во-первых, попробуйте воспринимать любую рабочую ситуацию «сверху», из позиции наблюдателя. Такая позиция позволяет снизить эмоциональный накал, прибавить объективности и рассудочности нашему видению, увидеть ценностный и смысловой аспект проблемы.'
                     '\n\nВо-вторых, постоянная тревога – это сигнал бедствия. Если вы много тревожитесь, но не всегда понимаете причины, надо срочно разгадать и проанализировать истинные основания тревоги. Бывают случаи, когда «рабочая» тревога на самом деле маскируют тревогу, связанную, например, со скрытыми семейными трудностями. Осознание этого факта позволяет сфокусировать внимание и направить усилия на разрешение реальных проблем. Если же так и не удалось выявить причины тревоги, то это тоже результат. Осознание необоснованности собственного чувства может значительно облегчить симптомы тревожного состояния.'
                     '\n\nВ-третьих, тревожным людям полезно освоить такие упражнения по контролю своих состояний, как медитация, аутотренинг, йога, цигун, дыхательная гимнастика. Рекомендуем начать с предложенных упражнений',
                     parse_mode='html',
                     reply_markup=markup)


def Specialist(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Московский политех')
    btn2 = types.KeyboardButton('МГУ')
    btn3 = types.KeyboardButton('ГУУ')
    btn4 = types.KeyboardButton('АГУ')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Выберите своё учебное заведение', parse_mode='html', reply_markup=markup)


def Music(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Другая композиция')
    btn2 = types.KeyboardButton('Вернуться в меню')
    markup.add(btn1, btn2)
    Music = open('/opt/ReformYSbot/Music relax/' + random.choice(os.listdir('Music relax')), 'rb')
    bot.send_audio(message.chat.id, Music,
                   parse_mode='html',
                   reply_markup=markup)


def Back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Выбрать упражнение (разгрузка)')
    btn2 = types.KeyboardButton('Что-то беспокоит')
    btn3 = types.KeyboardButton('Музыка для расслабления')
    markup.add(btn1, btn2, btn3)
    mess = f'<b>{message.from_user.first_name}</b>, выберите что вас интересует'
    bot.send_message(message.chat.id, mess,
                     parse_mode='html',
                     reply_markup=markup)


bot.polling(none_stop=True)
