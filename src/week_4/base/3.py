import json
def mean_age(json_string):
    json_data  = json.loads(json_string)
    sum_age = 0
    for data in json_data:
        sum_age += data['age']
    dict  = {'mean_age': sum_age/len(json_data)}
    return json.dumps(dict)


string = """[
    {
        "name": "Петр",
        "surname": "Петров",
        "patronymic": "Васильевич",
        "age": 23,
        "occupation": "ойтишнек"
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "patronymic": "Петрович",
        "age": 24,
        "occupation": "дворник"
    }
]"""
print(mean_age(string))
