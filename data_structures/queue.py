class Queue:
    class Node:
        def __init__(self, item, next_):
            self.item = item
            self.next = next_

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n

    def enqueue(self, item):
        old_last = self.last
        self.last = self.Node(item, None)

        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.first.item
        self.first = self.first.next

        self.n -= 1

        if self.is_empty():
            self.last = None

        return item
