class MyQueue:

    def __init__(self):
        self.S1 = [] # 1 2 3 4 5
        self.S2 = []

    def push(self, x: int) -> None:
        self.S1.append(x)

    def pop(self) -> int:
        while len(self.S1) > 1:
            self.S2.append(self.S1.pop())
        
        first = self.S1.pop()

        while len(self.S2) > 0:
            self.S1.append(self.S2.pop())

        return first

    def peek(self) -> int:
        return self.S1[0]

    def empty(self) -> bool:
        return len(self.S1) == 0

class MyQueue1:

    def __init__(self):
        self.S1 = []   # Stack to handle push operations
        self.S2 = []   # Stack to handle pop/peek operations

    def push(self, x: int) -> None:
        self.S1.append(x)

    def pop(self) -> int:
        if not self.S2: # if S2 is empty
            while len(self.S1) > 0:
                self.S2.append(self.S1.pop())
        
        return self.S2.pop()
    
    def peek(self) -> int:
        if not self.S2:
            while len(self.S1) > 0:
                self.S2.append(self.S1.pop())
        
        return self.S2[-1]
    
    def empty(self) -> bool:
        return not self.S1 and not self.S2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()