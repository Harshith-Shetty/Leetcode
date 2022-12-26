class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lf = n-1
        for i in range(n - 2, -1, -1):
            if nums[i] >= n - i - 1 or nums[i] >= lf - i:
                lf = i
        return True if lf == 0 else False