class Stack:
    class Node:
        def __init__(self, item, next_):
            self.item = item
            self.next = next_

    def __init__(self):
        self.n = 0
        self.first = None

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        self.first = self.Node(item, old_first)
        self.n += 1

    def pop(self):
        if self.first is None:
            raise Exception("Stack is empty")

        item = self.first.item
        self.first = self.first.next
        self.n -= 1

        return item
