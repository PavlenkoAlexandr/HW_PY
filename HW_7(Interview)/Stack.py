class Stack:

    def __init__(self, *args):
        self.data = [*args]

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.insert(0, item)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)
