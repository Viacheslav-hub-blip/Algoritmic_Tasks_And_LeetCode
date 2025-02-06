class TaskQueue:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)

    def dequeue(self):
        if len(self.tasks) > 0:
            return f"{self.tasks.pop(0)} удалена из очереди."
        else:
            return "Очередь пуста."

    def peek(self):
        if len(self.tasks) > 0:
            return self.tasks[0]
        else:
            return "Очередь пуста."

    def is_empty(self):
        if len(self.tasks) == 0:
            return True
        else:
            return False


task_queue = TaskQueue()
task_queue.enqueue("Задача 1")
task_queue.enqueue("Задача 2")
print(task_queue.peek())  # Вывод: "Задача 1"
print(task_queue.dequeue())  # Вывод: "Задача 1 удалена из очереди."
print(task_queue.peek())  # Вывод: "Задача 2"
print(task_queue.dequeue())  # Вывод: "Задача 2 удалена из очереди."
print(task_queue.dequeue())  # Вывод: "Очередь пуста."
