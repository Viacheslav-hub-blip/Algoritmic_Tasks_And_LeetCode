import datetime


class Meeting:
    def __init__(self, name, date: datetime.date, start_time: datetime.time, duration: int):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.participants = []

    @property
    def end_time(self):
        tm1 = datetime.timedelta(hours=self.start_time.hour)
        if self.duration % 60 == 0:
            tm2 = datetime.timedelta(hours=self.duration // 60)
        else:
            tm2 = datetime.timedelta(minutes=self.duration)
        tm_res = tm1 + tm2
        hours = int(datetime.timedelta.__str__(tm_res).split(':')[0])
        minutes = int(datetime.timedelta.__str__(tm_res).split(':')[1])
        return datetime.time(hour=hours, minute=minutes)

    def get_participants(self):
        res = []
        for participant in self.participants:
            res_strr = f"{participant.name}"
            res.append(res_strr)
        return res


class Employee:
    def __init__(self, name):
        self.name = name
        self.schedule: list[Meeting] = []

    def add_meeting(self, meeting: Meeting):
        new_start  = datetime.timedelta(hours=meeting.start_time.hour)
        new_end = datetime.timedelta(hours=meeting.end_time.hour)

        for meet in self.schedule:
            meet_start  = datetime.timedelta(hours=meet.start_time.hour)
            meet_end  = datetime.timedelta(hours=meet.end_time.hour)
            if meeting.date  == meet.date:
                #если новая встреча вложена в старую
                if new_start >= meet_start and new_end <= meet_end:
                    return False
                #если начинается раньше, но заканчивается во время существующей
                elif new_start < meet_start and (meet_start <= new_end <= meet_end):
                    return False
                #если новая встреча начинается во время существующей
                elif meet_start <= new_start <= meet_end:
                    return False
        meeting.participants.append(self)
        self.schedule.append(meeting)

    def get_schedule(self):
        res = []
        for meeting in self.schedule:
            res_str = f"{meeting.date} {(meeting.start_time.__str__()).split(':')[0]}:{(meeting.start_time.__str__()).split(':')[1]} - {(meeting.end_time.__str__()).split(':')[0]}:{(meeting.end_time.__str__()).split(':')[1]}: {meeting.name}"
            res.append(res_str)
        return res


meeting1 = Meeting("Встреча с клиентом", datetime.date(2024, 9, 10), datetime.time(10, 0), 60)
meeting3 = Meeting("Встреча с клиентом", datetime.date(2024, 9, 10), datetime.time(9, 0), 120)
meeting2 = Meeting("Планерка", datetime.date(2024, 9, 11), datetime.time(14, 0), 30)

employee1 = Employee("Борис Петров")
employee2 = Employee("Иван Иванов")

employee1.add_meeting(meeting1)
employee1.add_meeting(meeting3)
employee2.add_meeting(meeting2)

print(employee1.get_schedule())  # Выведет ['2024-09-10 10:00 - 11:00: Встреча с клиентом']
print(employee2.get_schedule())

employee1.add_meeting(meeting2)

print(meeting2.get_participants())
