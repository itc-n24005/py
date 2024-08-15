class Stack:
    def init(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise Exception("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return not self.items

stack = Stack()
stack.push(1)
value1 = stack.pop()
value2 = stack.pop()
print(f"1回目の所得: {value1}")
print(f"2回目の所得: {value2}")
print(f"現在のスタック: {stack.items}")
