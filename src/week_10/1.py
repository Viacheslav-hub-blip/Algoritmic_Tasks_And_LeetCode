class BrowserHistory:

    def __init__(self):
        self.history = []

    def visit(self, url):
        self.history.append(url)

    def back(self):
        if len(self.history) != 0:
            self.history.pop(-1)

    def show_current(self):
        if len(self.history) != 0:
            return self.history[-1]

    def show_history(self):
        if len(self.history) != 0:
            return self.history


history = BrowserHistory()
print(history.show_history())
print(history.show_current())
history.visit("https://www.example.com")
history.visit("https://www.google.com")
history.visit("https://www.wikipedia.org")

print(
    history.show_history())  # Вывод: ['https://www.example.com', 'https://www.google.com', 'https://www.wikipedia.org']
print(history.show_current())  # Вывод: https://www.wikipedia.org

history.back()
print(history.show_history())  # Вывод: ['https://www.example.com', 'https://www.google.com']
print(history.show_current())  # Вывод: https://www.google.com

history.back()
print(history.show_history())  # Вывод: ['https://www.example.com']
print(history.show_current())  # Вывод: https://www.example.com

print("-----------------")
history2 = BrowserHistory()
print(history2.show_history())
print(history2.show_current())