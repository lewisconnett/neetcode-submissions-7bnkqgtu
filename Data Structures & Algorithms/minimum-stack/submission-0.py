class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.min_val:
            self.min_val = float('inf')
            for num in self.stack:
                if num < self.min_val:
                    self.min_val = num


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
