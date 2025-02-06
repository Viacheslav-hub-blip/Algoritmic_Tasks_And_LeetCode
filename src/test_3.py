n, t = map(int, input().split(' '))  # количество сотрудников и время, когда уходит сотрудник
floors = list(map(int, input('').split(' ')))  # этажи
chelic_number = int(input(''))  # номер сотрудника

time_for_chel = 0  # сколько подниматься до чела
current_floor = floors[0]  # текущий этаж
last_floor = floors[0]  # предыдущий этаж

for floor in floors[1:chelic_number]:
    last_floor = current_floor
    current_floor = floor
    time_for_chel += abs(current_floor - last_floor)

all_time = 0
if time_for_chel > t:
    # получается мы не успеем к челику если высадимся на первом этаже
    # сначала едем к челику

    current_floor = floors[chelic_number]
    floors.pop(chelic_number)  # удли этот эиаж из списка
    all_time += abs(current_floor - floors[0])

    current_floor = floors[0]
    last_floor = floors[0]

    for floor in floors:
        last_floor = current_floor
        current_floor = floor

        all_time += abs(last_floor - current_floor)
else:
    current_floor = floors[0]
    last_floor = floors[0]

    for floor in floors:
        last_floor = current_floor
        current_floor = floor

        all_time += abs(last_floor - current_floor)

print(all_time)
