class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def Enough(capacity): 
            count = 1
            max = capacity
            for weight in weights:
                if weight > max:
                    max = capacity
                    count += 1
                max -= weight
            return True if count <= days else False

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if Enough(mid):
                right = mid
            else:
                left = mid + 1
        return left