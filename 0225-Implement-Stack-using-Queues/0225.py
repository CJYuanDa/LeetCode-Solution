class MyStack:

    def __init__(self):
        self.Q1, self.Q2 = [], []

    def push(self, x: int) -> None:
        self.Q1.append(x)

    def pop(self) -> int:
        for index, value in enumerate(self.Q1):
            if index == len(self.Q1) - 1:
                last = value
            else:
                self.Q2.append(value)
        self.Q1 = self.Q2
        self.Q2 = []
        return last

    def top(self) -> int:
        return self.Q1[-1]

    def empty(self) -> bool:
        return len(self.Q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()