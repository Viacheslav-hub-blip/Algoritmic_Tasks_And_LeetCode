import datetime


class Time:

    def __init__(self, *args):

        if len(args) == 1:
            hour = int(args[0][:2])
            min = int(args[0][3:5])
            if 0 <= hour <= 23 and 0 <= min <= 59:

                if len(args[0]) == 5:
                    self.time = args[0]
                elif len(args[0]) == 8:
                    hour = int(args[0][:2])
                    min = int(args[0][3:5])
                    sp = args[0][:-3].split(':')
                    if 0 <= hour <= 12 and 0 <= min <= 59:
                        if args[0][-2:] == 'PM':
                            self.time = f"{str(int(sp[0]) + 12)}:{sp[1]}"
                        elif args[0][-2:] == 'AM':
                            self.time = f"{sp[0]}:{sp[1]}"
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError

        elif len(args) == 2:
            if 0 <= args[0] <= 23 and 0 <= args[1] <= 59:
                if args[1] == 0:
                    self.time = f"{args[0]}:{args[1]}0"
                else:
                    self.time = f"{args[0]}:{args[1]}"
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def hours(self):
        return int(self.time.split(':')[0])

    @property
    def minutes(self):
        return int(self.time.split(':')[1])

    def is_night(self):
        if (int(self.time.split(':')[0]) >= 22 and int(self.time.split(':')[1]) >= 0) or (int(self.time.split(':')[0]) < 6):
            return True
        elif int(self.time.split(':')[0]) == 6 and int(self.time.split(':')[1]) == 0:
            return True
        elif int(self.time.split(':')[0]) == 6 and int(self.time.split(':')[1]) > 0:
            return False
        else:
            return False

    def difference(self, other):
        current_total_min = self.hours * 60 + self.minutes
        other_total_min = other.hours * 60 + other.minutes
        return abs(current_total_min - other_total_min)

    def __add__(self, other):
        if isinstance(other, int):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            datetime_format += datetime.timedelta(minutes=other)
            return Time(datetime_format.hour, datetime_format.minute)
        elif isinstance(other, str):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            other_datetime_format = datetime.datetime.strptime(other, "%H:%M")
            time_delta = datetime.timedelta(hours=other_datetime_format.hour, minutes=other_datetime_format.minute)
            new_date = datetime_format + time_delta
            return Time(new_date.hour, new_date.minute)
        elif isinstance(other, Time):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            timedelta = datetime.timedelta(hours=other.hours, minutes=other.minutes)
            new_date = datetime_format + timedelta
            return Time(new_date.hour, new_date.minute)

    def __sub__(self, other):
        if isinstance(other, int):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            total_min = self.total_minutes(datetime_format)
            if total_min - other < 0:
                raise ValueError
            new_date = datetime_format - datetime.timedelta(minutes=other)
            return Time(new_date.hour, new_date.minute)
        elif isinstance(other, str):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            other_datetime_format = datetime.datetime.strptime(other, "%H:%M")
            total_min_1  = self.total_minutes(datetime_format)
            total_min_2  = self.total_minutes(other_datetime_format)
            if total_min_1 - total_min_2 < 0:
                raise ValueError
            time_delta = datetime.timedelta(hours=other_datetime_format.hour, minutes=other_datetime_format.minute)
            new_date = datetime_format - time_delta
            return Time(new_date.hour, new_date.minute)
        elif isinstance(other, Time):
            datetime_format = datetime.datetime.strptime(self.time, "%H:%M")
            total_min = self.total_minutes(datetime_format)
            total_min_2  = other.hours * 60 + other.minutes
            if total_min - total_min_2 < 0:
                raise ValueError
            timedelta = datetime.timedelta(hours=other.hours, minutes=other.minutes)
            new_date = datetime_format - timedelta
            return Time(new_date.hour, new_date.minute)

    def __str__(self):
        return self.time

    def __eq__(self, other):
        if isinstance(other, Time):
            if self.hours == other.hours and self.minutes == other.minutes:
                return True
            else:
                return False
        elif isinstance(other, str):
            other_hour, other_minute = int(other.split(':')[0]), int(other.split(':')[1])
            if self.hours == other_hour and self.minutes == other_minute:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, Time):
            if self.hours > other.hours:
                return True
            elif self.hours == other.hours:
                if self.minutes > other.minutes:
                    return True
                else:
                    return False
            elif self.hours < other.hours:
                return False
        elif isinstance(other, str):
            other_hour, other_minute = int(other.split(':')[0]), int(other.split(':')[1])
            if self.hours > other_hour:
                return True
            elif self.hours == other_hour:
                if self.minutes > other_minute:
                    return True
                else:
                    return False
            elif self.hours < other_hour:
                return False

    def __lt__(self, other):
        if isinstance(other, Time):
            if self.hours < other.hours:
                return True
            elif self.hours == other.hours:
                if self.minutes < other.minutes:
                    return True
                else:
                    return False
            elif self.hours > other.hours:
                return False
        elif isinstance(other, str):
            other_hour, other_minute = int(other.split(':')[0]), int(other.split(':')[1])
            if self.hours < other_hour:
                return True
            elif self.hours == other_hour:
                if self.minutes < other_minute:
                    return True
                else:
                    return False
            elif self.hours > other_hour:
                return False

    def total_minutes(self, time):
        return time.hour * 60 + time.minute


#Пример операций с целым числом (минутами)
print(Time("12:30") + 45)  # Результат: 13:15
print(Time(14, 15) - 30 ) # Результат: 13:45
print(Time("06:30 AM") + 30)  # Результат: 07:00

print('--------------')
#Пример операций с другим объектом Time

print(Time("11:30 PM") + Time("02:15")) # Результат: 01:45
print(Time("02:30 PM") - Time("02:45"))  # Результат: 11:45

#Пример операции с строкой
print(Time("13:30") + "02:30") # Результат: 16:00