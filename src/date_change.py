import datetime
import calendar

s_date  = datetime.datetime.strptime(input(), '%d-%m-%Y')
s_date = datetime.datetime.strftime(s_date,'%Y-%m-%d')

s_date  = datetime.datetime.strptime(s_date, '%Y-%m-%d')
s_lang  = input()

day = s_date.weekday()
dates_ru = {0:'Понедельник', 1:'Вторник', 2:'Среда', 3:'Четверг', 4:"Пятница", 5:'Суббота', 6:'Воскресенье'}

dates_en = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:"Friday", 5:'Saturday', 6:'Sunday'}

if s_lang == 'ru':
    print('День недели -', dates_ru[day])
elif s_lang == 'en':
    print('Day of the week -', dates_en[day])
else:
    print('Непонятный язык')