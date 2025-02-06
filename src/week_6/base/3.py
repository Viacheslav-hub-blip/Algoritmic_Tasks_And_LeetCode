from datetime import datetime
from api import register_booking
import json


class Booking:
    def __init__(self, room_name: str, start: datetime, end: datetime):
        self.room_name = room_name
        self.start = start
        self.end = end

        if end < start:
            raise ValueError

    @property
    def duration(self):
        return int((self.end - self.start).total_seconds() / 60)

    @property
    def start_date(self):
        return datetime.strftime(self.start, '%Y-%m-%d')

    @property
    def end_date(self):
        return datetime.strftime(self.end, '%Y-%m-%d')

    @property
    def start_time(self):
        return datetime.strftime(self.start, '%H:%M')

    @property
    def end_time(self):
        return datetime.strftime(self.end, '%H:%M')

    def create_booking(self, room_name, start, end) -> str:
        print('Начинаем создание бронирования')
        new_booking = Booking(room_name, start, end)
        try:
            result = register_booking(new_booking)

            if result:
                result_dict = {"created": 'true',
                               'msg': 'Бронирование создано',
                               "booking": {
                                   "room_name": new_booking.room_name,
                                   "start_date": new_booking.start_date,
                                   "start_time": new_booking.start_time,
                                   "end_date": new_booking.end_date,
                                   "end_time": new_booking.end_time,
                                   "duration": new_booking.duration

                               }
                               }
                return json.dumps(result_dict)
            else:
                result_dict = {"created": 'false',
                               'msg': 'Комната занята',
                               "booking": {
                                   "room_name": new_booking.room_name,
                                   "start_date": new_booking.start_date,
                                   "start_time": new_booking.start_time,
                                   "end_date": new_booking.end_date,
                                   "end_time": new_booking.end_time,
                                   "duration": new_booking.duration

                               }
                               }
                return json.dumps(result_dict)
        except KeyError:
            result_dict = {"created": 'false',
                           'msg': 'Комната не найдена',
                           "booking": {
                               "room_name": new_booking.room_name,
                               "start_date": new_booking.start_date,
                               "start_time": new_booking.start_time,
                               "end_date": new_booking.end_date,
                               "end_time": new_booking.end_time,
                               "duration": new_booking.duration

                           }
                           }
            return json.dumps(result_dict)
        finally:
            print('Заканчиваем создание бронирования')


booking = Booking("Вагнер",
                  datetime(2022, 9, 1, 14),
                  datetime(2022, 9, 1, 15, 15))

print(booking.room_name)
print(booking.start)
print(booking.end)
print(booking.duration)
print(booking.start_date)
print(booking.end_date)
print(booking.start_time)
