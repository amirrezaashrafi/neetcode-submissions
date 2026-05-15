class Solution:
    def is_possible(self, piles, k, h):
        total_hour = sum((pile + k - 1) // k for pile in piles)
        return total_hour <= h 

    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left <= right:
            k = (left + right) // 2
            if self.is_possible(piles, k, h):
                right = k - 1
            else:
                left = k + 1

        return left