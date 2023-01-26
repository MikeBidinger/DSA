class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("Pushed:", item)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
            return
        item = self.stack[-1]
        self.stack.pop(-1)
        print("Popped:", item)

    def get_top(self):
        if self.isEmpty():
            return "Stack is empty!"
        return len(self.stack) - 1

    def printStack(self):
        if self.isEmpty():
            print("Stack is empty!")
            return
        print("Stack (Index : Item):")
        for idx, item in enumerate(self.stack):
            print("", idx, ":", item)


if __name__ == "__main__":

    # Create a stack
    stack = Stack()

    # Add items to stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Remove item from stack
    stack.pop()
    stack.push(40)

    # Get top of stack
    print("Top; Index:", stack.get_top(), 
                "Item:", stack.stack[stack.get_top()])

    # Print stack
    stack.printStack()
