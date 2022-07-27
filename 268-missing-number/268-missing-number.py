class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        sum = 0
        for x in nums:
            n = n + 1
            sum = sum + x
            
        val = int(n*(n+1)/2 - sum)
        return val