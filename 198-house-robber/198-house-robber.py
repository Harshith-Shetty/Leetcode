class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0, 0] + nums
        for i in range(3, len(nums)):
            b3 = nums[i-3] + nums[i]
            b2 = nums[i-2] + nums[i]
            nums[i] = max(b3, b2)
        return max(nums)