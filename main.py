from random import random, randint
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload, VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, timedelta, date
import requests
from bs4 import BeautifulSoup as bs
import re
import time
from vk_api.keyboard import VkKeyboard
from PIL import ImageGrab, Image
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


CLIENT_ID = "514c1aaca1f2c57"

#vk_session = VkApi(token="vk1.a.A5gdd12fvJYC5B0v0dupAQTVh-3JwwZjwermEOzsCkcJdln1VgSczNQeCSjziC3gR6DIAEwWBh6V2_lzV_VTopn0DsRUgo8cEdACI9xX08ZLZ77jJnYv4MhPZ1Q2ok1bYXzwRKwAguZId7d7lWgQVDXP62koJWST4yMS9pzzGalipfd0zKFWj_xeJg4vGe65TRUYnMkMwE_dzX7_9FuP2g")
vk_session = VkApi(token="vk1.a.IHYzHdSYguHT62BgxmP5sK2_uHWDoIRnw3vP8jN_gzxDvKrF9hiVUhzupGkUxxZ0HQvRS8sMA1qE7QNpXFWi7FoodtBnLm6DDikkzjVXPhZKyL0dq_Vyg5EGJIOhlP0JWU5B8q3O-243VUItxP6ktRwBpA1bX6hLOzpD-A5xOERLxQhfPKYKvwpwxMMATkLDSjRVbb6QD9CZuFDX1yyVrg")

#longpoll = VkBotLongPoll(vk_session, "218710682")
longpoll = VkBotLongPoll(vk_session, "218586481")

give = vk_session.get_api()
longpoll1 = VkLongPoll(vk_session)

vk = vk_session.get_api()

#bh = VkApi(token="vk1.a.A5gdd12fvJYC5B0v0dupAQTVh-3JwwZjwermEOzsCkcJdln1VgSczNQeCSjziC3gR6DIAEwWBh6V2_lzV_VTopn0DsRUgo8cEdACI9xX08ZLZ77jJnYv4MhPZ1Q2ok1bYXzwRKwAguZId7d7lWgQVDXP62koJWST4yMS9pzzGalipfd0zKFWj_xeJg4vGe65TRUYnMkMwE_dzX7_9FuP2g")
bh = VkApi(token="vk1.a.IHYzHdSYguHT62BgxmP5sK2_uHWDoIRnw3vP8jN_gzxDvKrF9hiVUhzupGkUxxZ0HQvRS8sMA1qE7QNpXFWi7FoodtBnLm6DDikkzjVXPhZKyL0dq_Vyg5EGJIOhlP0JWU5B8q3O-243VUItxP6ktRwBpA1bX6hLOzpD-A5xOERLxQhfPKYKvwpwxMMATkLDSjRVbb6QD9CZuFDX1yyVrg")
def buttons(user_id, message, keys):
    bh.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randint(1e16, 1e18), 'keyboard': keys})

def write_msg(user_id, message):
    bh.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randint(1e16, 1e18)})

def write_msg1(user_id, message, attachment):
    bh.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': attachment, 'random_id': randint(1e16, 1e18)})

def write_msg_to_chat(random_id, chat_id, message):
    vk.messages.send(random_id=random_id, chat_id=chat_id, message=message)

def todaySchedule():
    dateNowWeek = datetime.now()
    dateNowWeek1 = datetime.isoweekday(dateNowWeek)

    if dateNowWeek1 == 1:
        dateNowWeekStart = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 2:
        dateNowWeekStart = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 3:
        dateNowWeekStart = (dateNowWeek - timedelta(days=2)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 4:
        dateNowWeekStart = (dateNowWeek - timedelta(days=3)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 5:
        dateNowWeekStart = (dateNowWeek - timedelta(days=4)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 6:
        dateNowWeekStart = (dateNowWeek - timedelta(days=5)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 7:
        dateNowWeekStart = (dateNowWeek - timedelta(days=6)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')

    pageNowWeek = requests.get(
        f"https://www.asu.ru/timetable/students/20/2129440714/?date={dateNowWeekStart}-{dateNowWeekEnd}").text

    soup = bs(pageNowWeek, 'html.parser')

    # Переменная для определения сегодняшнего дня
    today = ''

    # Номер пары сейчас:
    url = soup.find('div', {'title': 'сейчас'})

    linkIndex = 0
    e = ''
    nowPair = ''

    for link1 in soup.find_all('span', {'class': 'schedule_table-date'}):
        linkIndex += 1

        # Расписание на сегодня (дата)

        # Расписание на сегодня ПН
        if link1.text.count("сегодня") == 1:
            todayDay = link1.find('span', class_='schedule_table-date-wd').text

            if todayDay == "пн" and dateNowWeek1 == 1:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                mondayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = mondayRasp[0].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"


            # Расписание на сегодня ВТ

            # Расписание на сегодня (дата)

            if todayDay == "вт" and dateNowWeek1 == 2:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                tuesdayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = tuesdayRasp[1].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"


            # Расписание на сегодня СР

            # Расписание на сегодня (дата)
            if todayDay == "ср" and dateNowWeek1 == 3:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                wednesdayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = wednesdayRasp[2].text
                d = c.split()

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"

            # Расписание на сегодня ЧТ

            # Расписание на сегодня (дата)

            if todayDay == "чт" and dateNowWeek1 == 4:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                thursdayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = thursdayRasp[3].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"


            # Расписание на сегодня ПТ

            # Расписание на сегодня (дата)

            if todayDay == "пт" and dateNowWeek1 == 5:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                fridayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = fridayRasp[4].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"



            # Расписание на сегодня СБ

            # Расписание на сегодня (дата)

            if todayDay == "сб" and dateNowWeek1 == 5:
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                saturdayRasp = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = saturdayRasp[5].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                nowPair += e
                if url != None:
                    nowPair += "\nСейчас идет: " + url.text + " пара"
                else:
                    nowPair += "\nНа сегодня пары закончились или не начались. =)"

            if today == 1:
                return "\n\n-------------------------------------------------------\n" + f"Расписание на сегодня {'(' + todayDate + ')'}:\n\n{nowPair}" + "\n\n-------------------------------------------------------\n"
        if dateNowWeek1 == 7:
            return "Сегодня ВС, введи: 'завтра/следующая', чтобы узнать расписание."

def scheduleTomorrow():
    # Нахождение пар на завтра
    now = datetime.now()


    today = date.today()
    tomorrow = today + timedelta(days=1)
    tomorrow = tomorrow.strftime('%d.%m')
    dayNext = 0

    dateNowWeek = datetime.now()
    dateNowWeek1 = datetime.isoweekday(dateNowWeek)

    if dateNowWeek1 == 1:
        dateNowWeekStart = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 2:
        dateNowWeekStart = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 3:
        dateNowWeekStart = (dateNowWeek - timedelta(days=2)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 4:
        dateNowWeekStart = (dateNowWeek - timedelta(days=3)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 5:
        dateNowWeekStart = (dateNowWeek - timedelta(days=4)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 6:
        dateNowWeekStart = (dateNowWeek - timedelta(days=5)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')
    elif dateNowWeek1 == 7:
        dateNowWeekStart = (dateNowWeek - timedelta(days=6)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=7)).strftime('%Y%m%d')

    pageNowWeek = requests.get(
        f"https://www.asu.ru/timetable/students/20/2129440714/?date={dateNowWeekStart}-{dateNowWeekEnd}").text

    soup = bs(pageNowWeek, 'html.parser')

    pairsTomorrow = ''

    for day in soup.find_all('span', class_='schedule_table-date-dm'):
        dayNext += 1
        if tomorrow == day.text:
            for link1 in soup.find_all('span', {'class': 'schedule_table-date'}):
                todayDate = link1.find('span', class_='schedule_table-date-dm').text
                today = link1.text
                today = today.count(todayDate)

                tomorrowSchedule = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

                c = tomorrowSchedule[dayNext - 1].text
                d = c.split()
                e = ''

                for i in d:
                    e += i + " "

                # Рег. выражения для удаления лишних строк (расписание сегодня)
                e = re.sub(
                    " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                    "\n\n", e)
                e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                           "\n\n", e)
                e = re.sub("преп. ", "", e)

                pairsTomorrow += e
                if today == 1:
                    print()
                else:
                    return "Возникла какая-то ошибка("
                break
    return "\n\n-------------------------------------------------------\n" + f"Текущая дата и время {now:%d.%m.%Y %H:%M}\n\n" + f"Расписание на завтра {'(' + tomorrow + ')'}:\n\n{pairsTomorrow}" + "\n\n-------------------------------------------------------\n"

def scheduleWeek():
    dateNowWeek = datetime.now()
    dateNowWeek1 = datetime.isoweekday(dateNowWeek)

    if dateNowWeek1 == 1:
        dateNowWeekStart = (dateNowWeek - timedelta(days=0)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 2:
        dateNowWeekStart = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 3:
        dateNowWeekStart = (dateNowWeek - timedelta(days=2)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 4:
        dateNowWeekStart = (dateNowWeek - timedelta(days=3)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 5:
        dateNowWeekStart = (dateNowWeek - timedelta(days=4)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 6:
        dateNowWeekStart = (dateNowWeek - timedelta(days=5)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')
    elif dateNowWeek1 == 7:
        dateNowWeekStart = (dateNowWeek - timedelta(days=6)).strftime('%Y%m%d')
        dateNowWeekEnd = (datetime.strptime(dateNowWeekStart, '%Y%m%d') + timedelta(days=6)).strftime('%Y%m%d')

    pageNowWeek = requests.get(
        f"https://www.asu.ru/timetable/students/20/2129440714/?date={dateNowWeekStart}-{dateNowWeekEnd}").text

    soup = bs(pageNowWeek, 'html.parser')

    scheduleThisWeek = ''
    e = ''
    linkIndex = 0
    arrSchedule = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

    for link1 in soup.find_all('span', {'class': 'schedule_table-date'}):
        linkIndex += 1
        dayWeek = link1.find('span', class_='schedule_table-date-wd').text
        dateWeek = link1.find('span', class_='schedule_table-date-dm').text
        c = arrSchedule[linkIndex-1].text
        d = c.split()
        e = "\n\n-------------------------------------------------------\n" + dayWeek.upper() + " " + dateWeek + "\n\n"

        for i in d:
            e += i + " "

        # Рег. выражения для удаления лишних строк (расписание сегодня)
        e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ", "\n\n", e)
        e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                   "\n\n", e)
        e = re.sub("преп. \n", "", e)

        scheduleThisWeek += e + "\n"
    return scheduleThisWeek + "\n\n-------------------------------------------------------\n"

def scheduleNextWeek():
    dateNowWeek = datetime.now()
    dateNowWeek1 = datetime.isoweekday(dateNowWeek)

    if dateNowWeek1 == 1:
        dateNextWeek = (dateNowWeek - timedelta(days=0)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 2:
        dateNextWeek = (dateNowWeek - timedelta(days=1)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 3:
        dateNextWeek = (dateNowWeek - timedelta(days=2)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 4:
        dateNextWeek = (dateNowWeek - timedelta(days=3)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 5:
        dateNextWeek = (dateNowWeek - timedelta(days=4)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 6:
        dateNextWeek = (dateNowWeek - timedelta(days=5)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)
    elif dateNowWeek1 == 7:
        dateNextWeek = (dateNowWeek - timedelta(days=6)).strftime('%Y%m%d')
        dateNextWeekStart = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=7)
        dateNextWeekEnd = datetime.strptime(dateNextWeek, '%Y%m%d') + timedelta(days=13)

    pageNextWeek = requests.get(
        f"https://www.asu.ru/timetable/students/20/2129440714/?date={dateNextWeekStart:%Y%m%d}-{dateNextWeekEnd:%Y%m%d}").text

    soup = bs(pageNextWeek, 'html.parser')

    e = ''
    scheduleNextWeek = ''
    linkIndex = 0
    arrSchedule = soup.find_all('div', class_="schedule_table-body-rows_group-rows")

    for link1 in soup.find_all('span', {'class': 'schedule_table-date'}):
            linkIndex += 1
            dayWeek = link1.find('span', class_='schedule_table-date-wd').text
            dateWeek = link1.find('span', class_='schedule_table-date-dm').text
            c = arrSchedule[linkIndex-1].text
            d = c.split()
            e = "\n\n-------------------------------------------------------\n" + dayWeek.upper() + " " + dateWeek + '\n\n'

            for i in d:
                e += i + " "

            # Рег. выражения для удаления лишних строк (расписание сегодня)
            e = re.sub(
                " дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] свободные аудитории ",
                "\n\n", e)
            e = re.sub(" дата изменения: [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9] ",
                       "\n\n", e)
            e = re.sub("преп. \n", "", e)

            scheduleNextWeek += e + "\n"
    return scheduleNextWeek + "\n\n-------------------------------------------------------\n"


# def screenWeek():
#     date_now = datetime.datetime.now()
#     day_of_week = datetime.datetime.isoweekday(date_now)
#
#     date_start = (date_now - datetime.timedelta(days=day_of_week - 1)).strftime('%Y%m%d')
#     date_end = (datetime.datetime.strptime(date_start, '%Y%m%d') + datetime.timedelta(days=6)).strftime('%Y%m%d')
#
#     profile_path = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\neh80lc7.default'
#     options = Options()
#     options.add_argument('--headless')
#     options.set_preference('profile', profile_path)
#     service = Service(r'C:/Users/Administrator/BotVK/geckodriver.exe')
#     driver = Firefox(service=service, options=options)
#     driver.get(f"https://www.asu.ru/timetable/students/20/2129440714/?date={date_start}-{date_end}")
#     time.sleep(0.5)
#     try:
#         screenshot_path = f"C:/Users/Administrator/BotVK/screenshotWeek{date_start}-{date_end}.png"
#         driver.save_full_page_screenshot(screenshot_path)
#         im = Image.open(screenshot_path)
#         im_crop = im.crop((35, 685, 900, 2073))
#         im_crop.save(screenshot_path, quality=100)
#         driver.quit()
#     except Exception as e:
#         print(e)
#
#
#         #driver.set_window_size(1920, 1080)
#         #driver.fullscreen_window()
#         #driver.execute_script("document.body.style.zoom=.77")
#         #pyautogui.scroll(-550)
#         #time.sleep(.5)
#         #try:
#             #PATH = f"C:/Users/Administrator/BotVK/screenshotWeek{dateNowWeekStart}-{dateNowWeekEnd}.png"
#             #screen = pyautogui.screenshot(PATH, region=(400, 100, 820, 950))
#             #screen.save(PATH)
#         #except Exception as e:
#             #print(e)
#
#         upload = VkUpload(vk)
#         photo = upload.photo_messages(open(screenshot_path, 'rb'))
#         owner_id = photo[0]['owner_id']
#         photo_id = photo[0]['id']
#         access_key = photo[0]['access_key']
#         attachment = f'photo{owner_id}_{photo_id}_{access_key}'
#
#         # im = pyimgur.Imgur(CLIENT_ID)
#         # uploaded_image = im.upload_image(PATH, title=f"Week {dateNowWeekStart}-{dateNowWeekEnd}")
#         # answer = uploaded_image.link
#
#     except:
#         attachment = "Что-то пошло не так, попробуйте еще раз или посмотрите информацию в текстовом формате..."
#    # try:
#        # driver.close()
#     #except Exception as e:
#      #   print("Nothing to do with it")
#     return attachment

# def screenNextWeek():
    now = datetime.now()
    week_day = datetime.isoweekday(now)

    next_week_start = now + timedelta(days=(7 - week_day) % 7)
    next_week_end = next_week_start + timedelta(days=6)
    date_next_week = next_week_start.strftime("%Y%m%d")

    try:
        profile_path = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\neh80lc7.default'
        options = Options()
        options.add_argument('--headless')
        options.set_preference('profile', profile_path)
        service = Service(f'C:/Users/Administrator/BotVK/geckodriver.exe')
        driver = Firefox(service=service, options=options)
        driver.get(f"https://www.asu.ru/timetable/students/20/2129440714/?date={date_next_week}-{next_week_end.strftime('%Y%m%d')}")
        time.sleep(.5)
        try:
            driver.save_full_page_screenshot(
                f"C:/Users/Administrator/BotVK/screenshotWeek{date_next_week}-{next_week_end.strftime('%Y%m%d')}.png")
            im = Image.open(f"C:/Users/Administrator/BotVK/screenshotWeek{date_next_week}-{next_week_end.strftime('%Y%m%d')}.png")
            im_crop = im.crop((35, 685, 900, 2073))
            im_crop.save(f"C:/Users/Administrator/BotVK/screenshotWeek{date_next_week}-{next_week_end.strftime('%Y%m%d')}.png",
                         quality=100)
            driver.close()
        except Exception as e:
            print(e)

        upload = VkUpload(vk)
        photo = upload.photo_messages(open(f"C:/Users/Administrator/BotVK/screenshotWeek{date_next_week}-{next_week_end.strftime('%Y%m%d')}.png", 'rb'))
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        # os.remove(PATH)

        #im = pyimgur.Imgur(CLIENT_ID)
        #uploaded_image = im.upload_image(PATH, title=f"Week {dateNextWeekStart}-{dateNextWeekEnd}")
        #answer = uploaded_image.link

    except:
        attachment = "Что-то пошло не так, попробуйте еще раз или посмотрите информацию в текстовом формате..."
    #try:
   #     driver.close()
 #   except Exception as e:
  #      print("Nothing to do with it")
    return attachment

def testScreen():
    upload = VkUpload(vk)
    photo = upload.photo_messages(open('screenshotWeek20230130-20230205.png', 'rb'))
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment

def get_keys():
    menu = VkKeyboard()
    menu.add_button(label="Сегодня", color="positive") # NEGATIVE - red, SECONDARY - white, PRIMARY - blue, POSITIVE - green
    menu.add_button(label="Завтра", color="primary")
    menu.add_button(label="Текущая", color="positive")
    menu.add_line()
    menu.add_button(label="Следующая", color="primary")
    #menu.add_button(label="Скрин1", color="positive")
    #menu.add_button(label="Скрин2", color="primary")
    menu = menu.get_keyboard()
    return menu


while True:  # Нужно, чтобы функция была вечной
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                message = event.obj['message']
                text = message['text']
                text = text.replace("[", '').replace("|", '').replace(" ",'').replace(",", "").replace("@", "")
                text = re.sub(r'\w+\]', '', text)
                if text.lower() == 'сегодня' or text.lower() == "today":
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = todaySchedule()

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                    )
                elif text.lower() == 'завтра' or text.lower() == "tomorrow":
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = scheduleTomorrow()

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                    )
                elif text.lower() == 'текущая неделя' or text.lower() == "текущая":
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = scheduleWeek()

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                    )
                elif text.lower() == 'следующаянеделя' or text.lower() == "следующая":
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = scheduleNextWeek()

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                    )
                # elif text.lower() == 'скрин1':
                #     random_id = round(random() * 10 ** 9)
                #     chat_id = int(event.chat_id)
                #     message = "Расписание на эту неделю:"
                #     attachment = screenWeek()
                #
                #     vk.messages.send(
                #         random_id=random_id,
                #         chat_id=chat_id,
                #         message=message,
                #         attachment=attachment,
                #     )
                # elif text.lower() == 'скрин2':
                #     random_id = round(random() * 10 ** 9)
                #     chat_id = int(event.chat_id)
                #     message = "Расписание на следующую неделю:"
                #
                #     attachment = screenNextWeek()
                #
                #     vk.messages.send(
                #         random_id=random_id,
                #         chat_id=chat_id,
                #         message=message,
                #         attachment=attachment,
                #     )
                elif text.lower() == 'начать' or text.lower() == 'пуск' or text.lower() == 'команды' or text.lower() == 'старт' or text.lower() == 'кнопки' or text.lower() == 'кнопка':
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = "\n\n-------------------------------------------------------\n" + "Список доступных команд:\n\n'Сегодня' - расписание на сегодня (текстом)\n\n'Завтра' - расписание на завтра (текстом)\n\n'Текущая' - расписание на текущую неделю (текстом)\n\n'Следующая' - расписание на следующую неделю (текстом)\n\n"+ "-------------------------------------------------------\n"

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                        keyboard=get_keys()
                    )

                else:
                    random_id = round(random() * 10 ** 9)
                    chat_id = int(event.chat_id)
                    message = "\n\n-------------------------------------------------------\n" + "Я вас не понимаю! =(\n\nСписок доступных команд:\n\n'Сегодня' - расписание на сегодня (текстом)\n\n'Завтра' - расписание на завтра (текстом)\n\n'Текущая' - расписание на текущую неделю (текстом)\n\n'Следующая' - расписание на следующую неделю (текстом)\n\n" + "-------------------------------------------------------\n"

                    vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=message,
                    )

            elif event.type == VkBotEventType.MESSAGE_NEW:
                message = event.obj['message']
                text = message['text']
                if event.from_user:

                    # Получаем id пользователя
                    id = event.obj['message']['from_id']

                    if text.lower() == 'сегодня' or text.lower() == "today":
                        today = todaySchedule()
                        write_msg(id, f'{today}')

                    elif text.lower() == 'завтра' or text.lower() == "tomorrow":
                        tomorrow = scheduleTomorrow()
                        write_msg(id, f'{tomorrow}')

                    elif text.lower() == 'текущая неделя' or text.lower() == "текущая":
                        thisWeek = scheduleWeek()
                        write_msg(id, f'{thisWeek}')

                    elif text.lower() == 'следующая неделя' or text.lower() == "следующая":
                        nextWeek = scheduleNextWeek()
                        write_msg(id, f'{nextWeek}')

                    # elif text.lower() == 'скрин1':
                    #     message = "Расписание на эту неделю:"
                    #     screen = screenWeek()
                    #     write_msg1(id, message, screen)
                    #
                    # elif text.lower() == 'скрин2':
                    #     message = "Расписание на следующую неделю:"
                    #     screenNext = screenNextWeek()
                    #     write_msg1(id, message, screenNext)

                    elif text.lower() == 'начать' or text.lower() == 'пуск' or text.lower() == 'команды' or text.lower() == 'старт' or text.lower() == 'кнопки' or text.lower() == 'кнопка':
                        message = "\n\n-------------------------------------------------------\n" + "Список доступных команд:\n\n'Сегодня' - расписание на сегодня (текстом)\n\n'Завтра' - расписание на завтра (текстом)\n\n'Текущая' - расписание на текущую неделю (текстом)\n\n'Следующая' - расписание на следующую неделю (текстом)\n\n" + "-------------------------------------------------------\n"
                        buttons(id, message, get_keys())

                    else:
                        write_msg(id, "\n\n-------------------------------------------------------\n" + "Я вас не понимаю! =(\n\nСписок доступных команд:\n\n'Сегодня' - расписание на сегодня (текстом)\n\n'Завтра' - расписание на завтра (текстом)\n\n'Текущая' - расписание на текущую неделю (текстом)\n\n'Следующая' - расписание на следующую неделю (текстом)\n\n" + "-------------------------------------------------------\n")

    except Exception as error:
        print(error)  # Вывод ошибки, если она появляется