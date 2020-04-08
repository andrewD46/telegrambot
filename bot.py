#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import COVID19Py
import telebot

bot = telebot.TeleBot('976306774:AAEfFiDSbXpXCMZtg4Dgvn_6U7WuSVuE0yA')
covid19 = COVID19Py.COVID19()


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"Привет <b>{message.from_user.first_name}!👋</b>\nЯ помогу Вам оставаться в курсе ситуации с <b>COVID19</b> в мире!🦠\n" \
                f"Чтобы узнать данные про <b>COVID19</b> напишите название страны, например: Беларусь, Россия, США и тд.🌎\n\nЧтобы просмотреть доступные страны используйте команду /country"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['country'])
def country(message):
    send_mess = f"👋<b>Доступные страны🦠:</b>\n- Беларусь🇧🇾\n- Россия🇷🇺\n- США🇺🇸\n- Украина🇺🇦\n- Турция🇹🇷\n- Сирия🇸🇾\n- Ливан🇱🇧\n- Польша🇵🇱\n- Казахстан🇰🇿\n- Италия🇮🇹\n- Иран🇮🇷\n- Индия🇮🇳\n- Великобритания🇬🇧\n- Франция🇫🇷\n- Испания🇪🇸\n- Китай🇨🇳\n- Канада🇨🇦"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def user_mess(message):
    final_message = ''
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode('US')
        country = 'США🇺🇸'
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode('UA')
        country = 'Украина🇺🇦'
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode('RU')
        country = 'Россия🇷🇺'
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode('BY')
        country = 'Беларусь🇧🇾'
    elif get_message_bot == "турция":
        location = covid19.getLocationByCountryCode('TR')
        country = 'Турция🇹🇷'
    elif get_message_bot == "сирия":
        location = covid19.getLocationByCountryCode('SY')
        country = 'Сирия🇸🇾'
    elif get_message_bot == "польша":
        location = covid19.getLocationByCountryCode('PL')
        country = 'Польша🇵🇱'
    elif get_message_bot == "ливан":
        location = covid19.getLocationByCountryCode('LB')
        country = 'Ливан🇱🇧'
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode('KZ')
        country = 'Казахстан🇰🇿'
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode('IT')
        country = 'Италия🇮🇹'
    elif get_message_bot == "иран":
        location = covid19.getLocationByCountryCode('IR')
        country = 'Иран🇮🇷'
    elif get_message_bot == "индия":
        location = covid19.getLocationByCountryCode('IN')
        country = 'Индия🇮🇳'
    elif get_message_bot == "великобритания":
        location = covid19.getLocationByCountryCode('GB')
        country = 'Великобритания🇬🇧'
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode('FR')
        country = 'Франция🇫🇷'
    elif get_message_bot == "испания":
        location = covid19.getLocationByCountryCode('ES')
        country = 'Испания🇪🇸'
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode('DE')
        country = 'Германия🇩🇪'
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode('CN')
        country = 'Китай🇨🇳'
    elif get_message_bot == "канада":
        location = covid19.getLocationByCountryCode('CA')
        country = 'Канада🇨🇦'
    else:
        location = covid19.getLatest()
        final_message = f"К сожалению, я не понял Вас, либо данные по этой стране не доступны🥺\nДанные по всему миру 🌎:\n<b>Заболевших: </b>{location['confirmed']:,} 🤕\n<b>Смертей: </b>{location['deaths']:,} 😔\n\n<code>Источник</code> <a href='https://systems.jhu.edu/research/public-health/ncov/'>JHU CSSE</a>"

    if final_message == '' and country != 'Китай🇨🇳':
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"{country}:\nНаселение: {location[0]['country_population']:,} 👤\n" \
                        f"Последнее обновление: {date[0]} {time[0]} 🕘\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,} 🤕\n<b>Смертей: </b>" \
                        f"{location[0]['latest']['deaths']:,} 😔 " \
                        f"\n\n<code>Источник</code> <a href='https://systems.jhu.edu/research/public-health/ncov/'>JHU CSSE</a>"

    if final_message == ''and country == 'Китай🇨🇳':
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"{country}:\nНаселение: {location[0]['country_population']:,} 👤\n" \
                        f"Последнее обновление: {date[0]} {time[0]} 🕘\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,} 🤕\n<b>Смертей: </b>" \
                        f"{location[0]['latest']['deaths']:,} 😔 " \
                        f"\n\n<code>Источник</code> <a href='https://systems.jhu.edu/research/public-health/ncov/'>JHU CSSE</a>"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)

location = covid19.getLocationByCountryCode('EU')
