import telebot


bot = telebot.TeleBot('1360334701:AAGS91RhHQoZeRw7wklmwfs8QWaBAVwaNjw')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup(' True,True ')
keyboard1.row(' Привет', ' Дорожные знаки ' ' Поиск номеров ',
              ' Аукцион номеров')
keyboard1.row(' Именные номера', ' Блатные номера', ' Код регионов')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, " Привет ",
                                           + message.from_user.first_name)
    bot.send_message(message.from_user.id, " Выберите категорию",
                                           reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'код регионов':
        bot.send_message(message.chat.id, '01 г.Бишкек '
                                          '\n02 г.Ош '
                                          '\n03 Баткенская обл'
                                          '\n04 Джалал-Абадская обл'
                                          '\n05 Нарынская обл'
                                          '\n06 Ошская обл '
                                          '\n07 Талаская обл'
                                          '\n08 Чуйская обл'
                                          '\n09 Иссык-Кульская обл')
    elif message.text.lower() == 'блатные номера':
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIBk1-ZfuG8rsYLbbhGZKjSy'
                                        'P4CW9HbAAKUrzEbdRrQSJ8wHKOqpH3HSMnUly'
                                        '4AAwEAAwIAA3gAA_4rAgABGwQ')
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIBlF-ZfxkcYV4W8c5gTCLqj'
                                        'mTyQtTpAAKVrzEbdRrQSH3d_AdBfVuB7COlli'
                                        '4AAwEAAwIAA3kAA5w5AwABGwQ')
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIBlV-Zf2JA1CIz4hX3Wccj8'
                                        '2sXRwxtAAKWrzEbdRrQSDbVhict1tbfiV34lC'
                                        '4AAwEAAwIAA3kAA4RABgABGwQ')
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIBll-Zf5dbcYrxqOBIeFyNj'
                                        'Z6Jb24uAAKXrzEbdRrQSMntfHs2daTVRk3zly'
                                        '4AAwEAAwIAA3kAA65FAgABGwQ')
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIDgV-dQagSonnmlLZp0i_JS'
                                        'ftuiTIrAAIysjEbYmboSOtJJpI3c3E6nOU-li'
                                        '4AAwEAAwIAA3kAA_a_AwABGwQ', 'Примеры '
                                        'блатных номеров'
                                        '\nПо всем вопросам '
                                        'звонить 119')
    elif message.text.lower() == 'аукцион номеров':
        bot.send_message(message.chat.id, 'Нажми на ссылку https://nomer.srs.'
                                          'kg/public/auction/list.xhtml')
    elif message.text.lower() == 'поиск номеров':
        bot.send_message(message.chat.id, 'Нажми на ссылку https://nomer.srs.'
                                          'kg/public/plate/list.xhtml')
    elif message.text.lower() == 'именные номера':
        bot.send_message(message.chat.id, 'Госпредприятием «Инфоком» '
                                          'реализованы именные госномера по'
                                          'бишкекскому региону «VIP 01» и '
                                          '«LEXUS», стоимость каждого '
                                          'составляет 100 000 сом, при'
                                          'этом отметим, что вся сумма от '
                                          'реализации именных перечисляется'
                                          '1в республиканский бюджет.'
                                          'Стать обладателем именного '
                                          'номера можно любому гражданину, '
                                          'достаточно внести оплату через'
                                          'кассы банка, подать заявление в '
                                          'Департамент регистрации транспорта'
                                          'и водительского состава, также '
                                          'наличие документов на собственное'
                                          'авто. При этом изготовление именных'
                                          'знаков осуществляется с соблюдением'
                                          'следующих требований:пластина '
                                          'именного номерного знака должна '
                                          'иметь белый фон с изображением '
                                          'Государственного флага Кыргызской '
                                          'Республики; номер может содержать'
                                          'цифровые символы (арабские) и '
                                          'заглавные буквы латинского алфавита'
                                          'номер содержит как минимум две '
                                          'буквы, которые располагаются в '
                                          'начале именного номерного знака; '
                                          'именной номерной знак'
                                          'не должен содержит аббревиатуры '
                                          'государственных органов Кыргызской'
                                          'Республики;именной номерной знак не'
                                          'должен содержать комбинацию символо'
                                          'в'
                                          'представляющую собой: призыв к '
                                          'насильственному свержению или'
                                          'изменению существующего '
                                          'конституционного строя, нарушению'
                                          'суверенитета и территориальной'
                                          'целостности Кыргызской Республики и'
                                          'любого иного государства, к '
                                          'пропаганде войны, насилия и '
                                          'жестокости, национальной, '
                                          'религиозной исключительности и '
                                          'нетерпимости к другим народам и '
                                          'нациям; выражение, считающееся '
                                          'нецензурным. Напомним, что с 2016 '
                                          'года уполномоченным органом по '
                                          'реализации государственных номерных'
                                          'знаков является Государственное '
                                          'предприятие «Инфоком» при ГРС. '
                                          'Предприятием успешно реализован'
                                          'проект по проведению онлайн'
                                          'аукционов на госномера с особенной'
                                          'комбинацией цифр. Так, за прошедшее'
                                          'время продано 276 аукционных на '
                                          'сумму 9 361 381 сом и 3416 '
                                          'безаукционных номеров на сумму'
                                          '11 742 160 сом.Важно отметить, что'
                                          'при реализации регистрационных '
                                          'номерных знаков с особенной '
                                          'комбинацией цифр, поступления в '
                                          'госбюджет составляют 91% от чистой '
                                          'прибыли, а от именных номеров 100%.'
                                          '\nПО ВСЕМ ВОПРОСАМ ЗВОНИТЬ 119')
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIB11-bruucjgT8NNZ9t4InE'
                                        'ddfuUx8AAIvrzEbn8LgSFuliNKyv6dXdHlDli'
                                        '4AAwEAAwIAA3kAA0i3AwABGwQ',
                                        'Пример')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'дорожные знаки':
        bot.send_message(message.chat.id, 'Дорожные знаки \n1. Предупреждающие'
                                          'знаки\n2. Знаки приоритета\n3.'
                                          'Запрещающие знаки'
                                          '\n4. Предписывающие знаки'
                                          '\n5. Знаки особых предписаний'
                                          '\n6. Информационные знаки'
                                          '\n7. Знаки сервиса'
                                          '\n8.Знаки дополнительной информации'
                                          '(таблички)'
                                          '\n Значения знаков можете скачать '
                                          'по этой ссылке')

    else:
        bot.send_message(message.chat.id, 'Упс! У меня нет информации об этом')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBc1-Zc2Xj2cHJCrr2051'
                                          '231uPbYKGAAL4AAOPFmk0MEOOmdbcX'
                                          'i8bBA')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    print(message)
bot.polling()
