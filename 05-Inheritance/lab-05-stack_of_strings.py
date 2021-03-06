class Stack:
    def __init__(self, *args):
        self.data = [*args]

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(el for el in self.data[::-1])}]"

