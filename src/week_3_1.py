import datetime
from datetime import date


def sampling(month: int, birthdays):
    birthdays_in_month = {}
    for key, value in birthdays.items():
        if value.month == month:
            birthdays_in_month[key] = value
    return birthdays_in_month


def create_str(month: int,
               birthdays,
               budget: int,
               prize: int):
    str = f"Именинники в месяце {month}: "
    birthdays_with_new_format_date = {}

    for key, value in birthdays.items():
        new_date_format = datetime.datetime.strftime(value, "%d.%m.%Y")
        birthdays_with_new_format_date[key] = f"({new_date_format})"

    str = str + ', '.join(f'{key} {value}' for key, value in
                          birthdays_with_new_format_date.items()) + '.' + f' При бюджете {budget} они получат по {prize} рублей.'
    return str


def gift_count(budget: int,
               month: int,
               birthdays):

    # оставляем только тех у кого день рождения в нужном месяце
    birthdays_in_month = sampling(month, birthdays)

    # сортировка словаря по дням рождениям
    if len (birthdays_in_month) != 0:
        sorted_birthdays = dict(sorted(birthdays_in_month.items(), key=lambda x: datetime.datetime.strftime(x[1], '%m-%d')))
        result = create_str(month, sorted_birthdays, budget, int(budget / len(sorted_birthdays)))
        print(result)
    else:
        print('В этом месяце нет именинников.')



if __name__ == '__main__':
    str1 = 'Именинники в месяце 5: Рахимджон (06.05.1965), Орзухон (25.05.1999), Галя (30.05.1971). При бюджете 20000 они получат по 6666 рублей.'
    str2 = 'Именинники в месяце 5: Рахимджон (06.05.1965), Орзухон (25.05.1999), Галя (30.05.1971). При бюджете 20000 они получают по 6666 рублей.'
    workers = {
        "Катя": date(1989, 1, 1),
        "Ваня": date(1971, 1, 6),
        "Рахимджон": date(1965, 5, 6),
        "Орзухон": date(1999, 5, 25),
        "Галя": date(1971, 5, 30),
        "Владимир Владимирович": date(1952, 10, 7)}
    gift_count(20000, 5, workers)
