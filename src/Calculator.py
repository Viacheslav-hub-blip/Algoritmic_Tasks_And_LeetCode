from typing import  Union

T  = Union[int , float]
class Calculator:
    last = None

    def __init__(self):
        self.history_operations = []

    def _add_in_history(self, operation: str) -> None:
        self.history_operations.append(operation)
        Calculator.last = operation

    def sum(self, a: T, b: T) -> T:
        res  = a + b
        self._add_in_history(f"sum({a}, {b}) == {res}")
        return res

    def sub(self, a: T, b: T) -> T:
        res  = a - b
        self._add_in_history(f"sub({a}, {b}) == {res}")
        return res

    def mul(self, a: T, b: T) -> T:
        res = a * b
        self._add_in_history(f"mul({a}, {b}) == {res}")
        return res

    def div(self, a: T, b: T, mod=False) -> T:
        if mod:
            res  = a % b
            self._add_in_history(f"div({a}, {b}) == {res}")
            return res
        else:
            res  = a / b
            self._add_in_history(f"div({a}, {b}) == {res}")
            return res

    def history(self, n: int) -> Union[str, None]:
        if 0 <= n <= len(self.history_operations):
            return self.history_operations[-n]
        else:
            return None

    @classmethod
    def clear(cls):
        cls.last = None