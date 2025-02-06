def evaluate_test_attempt(test_data: dict, attempt_data: dict):
    user_id = attempt_data['user_id']
    date = attempt_data['date']
    score = 0
    for answer_number, answer in attempt_data['answers'].items():
        correct_answer = test_data['questions'][answer_number]['correct_answer']

        if answer == correct_answer:
            score += 1
    return {'user_id': user_id, 'date': date, 'score': score}


def create_rating_table(test_data: dict, attempt_data: []):
    users_data = []
    for current_attempt in attempt_data:
        users_data.append(evaluate_test_attempt(test_data, current_attempt))

    sorted_user_data = sort_user(users_data)

    users_data_pos = []
    for position, user in enumerate(sorted_user_data):
        users_data_pos.append(
            {'position': position + 1, 'user_id': user['user_id'], 'max_score': user['score'], 'date': user['date']})
    return users_data_pos


def sort_user(users_data: []):
    new_list = []
    id_with_score = {}
    for i in range(len(users_data)):
        if users_data[i]['user_id'] not in id_with_score.keys():
            id_with_score[users_data[i]['user_id']] = {'score': users_data[i]['score'], 'date': users_data[i]['date']}

        else:
            if users_data[i]['score'] > id_with_score.get(users_data[i]['user_id'])['score']:
                id_with_score[users_data[i]['user_id']] = {'score': users_data[i]['score'],
                                                           'date': users_data[i]['date']}

    for key, value in id_with_score.items():
        new_list.append({'user_id': key, 'score': value['score'], 'date': value['date']})

    new_list = sorted(new_list, key=lambda x: x['date'])
    new_list = sorted(new_list, key=lambda x: x['score'], reverse=True)
    print('new', new_list)
    return new_list

test_data = {
    'name': 'Тест по программированию',
    'questions': {
        1: {'type': 'multi_input', 'correct_answer': [1, 2, 3]},
        2: {'type': 'single_input', 'correct_answer': 1},
        3: {'type': 'text', 'correct_answer': 'Интерфейс программирования приложений'}
    }
}
attempts_data_1 = [
    {
        "user_id": 123,
        "date": "2024-03-15 10:30:45",
        "answers": {
            1: [2, 3],
            2: 1,
            3: "Интерфейс программирования приложений"
        }
    },
    {
        "user_id": 456,
        "date": "2024-03-16 12:00:10",
        "answers": {
            1: [1, 2],
            2: 1,
            3: "Интерфейс программирования приложений"
        }
    },
    {
        "user_id": 123,
        "date": "2024-03-17 15:00:04",
        "answers": {
            1: [1, 2, 3],
            2: 1,
            3: "Интерфейс программирования приложений"
        }
    }
]
print(create_rating_table(test_data, attempts_data_1))
