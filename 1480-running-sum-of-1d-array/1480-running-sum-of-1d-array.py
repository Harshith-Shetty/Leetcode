class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for x,y in enumerate(nums):
            nums[x] = sum + y
            sum = nums[x]
        return nums