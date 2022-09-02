class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        ans = self.stack[0]
        self.stack = self.stack[1:]
        return ans
        

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack
        