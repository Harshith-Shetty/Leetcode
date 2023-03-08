class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right
        while left <= right:
            rate_k = (left + right)  // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate_k)
            if hours <= h:
                min_k = min(min_k, rate_k)
                right = rate_k - 1
            else:
                left = rate_k + 1
        return min_k