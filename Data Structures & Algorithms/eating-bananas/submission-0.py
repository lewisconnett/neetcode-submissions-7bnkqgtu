class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            k = (left + right) // 2 

            time = self.eat_bananas(k, piles)

            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res

    def eat_bananas(self, k: int, piles: List[int]) -> int:
        total_time = 0
        for p in piles:
            total_time += math.ceil(p / k)
        
        return total_time