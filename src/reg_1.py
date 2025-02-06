import re


def is_valid_expression(expression):
    # Удалить пробелы
    expression = re.sub(r'\s', '', expression)

    # Проверить, что выражение состоит только из допустимых символов
    if not re.match(r'^[\d\+\-\*\/\(\)\.]+$', expression):
        return False

    if '()' in expression or ((expression.count('*') + expression.count('+') + expression.count('-') + expression.count('/')) == 0):
        return False

    # Проверить, что скобки правильно вложены
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    # Проверить, что операторы и операнды чередуются
    tokens = re.findall(r'\d+\.\d+|\d+|\+|-|\*|/|\(|\)', expression)

    if "".join(tokens) != expression:
        return False

    for i in range(len(tokens) - 1):
        if tokens[i] in '+-*/' and tokens[i + 1] in '+-*/.':
            return False
        if tokens[i] == '(' and tokens[i + 1] in '+-*/':
            return False
        if tokens[i] in '+-*/' and (tokens[i + 1] == ')'):
            return False
        if tokens[i+1] in '+-*/' and i+1 == len(tokens) - 1:
            return False
    return True
