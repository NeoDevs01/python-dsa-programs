import time

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

s = stack()
start = time.time()
print(s.isEmpty())
print("Push operation")
s.push(11)
s.push(12)
s.push(13)
print("Size:", s.size())
print(s.display())
print("Peek:", s.peek())
print("Pop operation")
print(s.pop())
print(s.pop())
print(s.display())
print("Size:", s.size())
end = time.time()
print("Runtime of the program is", end - start)
# End of P3.PY