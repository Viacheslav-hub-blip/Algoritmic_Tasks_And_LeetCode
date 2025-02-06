def evaluate_test_attempt(test_data: dict, attempt_data: dict):
    user_id = attempt_data['user_id']
    date = attempt_data['date']
    score  = 0
    for answer_number, answer in attempt_data['answers'].items():
        correct_answer  = test_data['questions'][answer_number]['correct_answer']
        if answer == correct_answer:
            score += 1
    return {'user_id': user_id, 'date': date, 'score': score}


test_data = {
    'name': 'Тест по программированию',
    'questions': {
        1: {'type': 'multi_input', 'correct_answer': [1, 2, 3]},
        2: {'type': 'single_input', 'correct_answer': 1},
        3: {'type': 'text', 'correct_answer': 'Интерфейс программирования приложений'}
    }
}

attempt_data = {
    'user_id': 123,
    'date': '2023-03-15 10:30:45',
    'answers': {
        1: [1, 2],
        2: 1,
        3: 'Интерфейс программирования приложений'
    }
}

print(evaluate_test_attempt(test_data, attempt_data))
