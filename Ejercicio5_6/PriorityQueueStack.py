from queue import PriorityQueue
class Stack:
    def __init__(self):
        self.count = 0
        self.stack = PriorityQueue()

    def push(self, value):
        self.count -= 1
        self.stack.put([self.count, value])

    def pop(self):
        if self.stack.empty():
            print("PILA VACIA!")
            return

        self.count += 1
        self.stack.get()

    def top(self):
        temp = self.stack.get()
        self.stack.put(temp)
        return temp[1]

    def isEmpty(self):
        return self.stack.empty()