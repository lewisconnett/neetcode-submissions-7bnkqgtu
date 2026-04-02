class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        self.memo[n] = result

        return self.memo[n]