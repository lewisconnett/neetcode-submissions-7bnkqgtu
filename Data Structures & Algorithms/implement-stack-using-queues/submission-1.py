class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        
        popped_element = self.queue1.pop(0)

        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

        return popped_element

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        if self.queue1:
            return False
        
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()