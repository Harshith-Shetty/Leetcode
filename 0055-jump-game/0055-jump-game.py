class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums[:-1] or len(nums) == 1: return True

        pt = nums.index(0)            

        for i in range(len(nums)):

            if i <= pt and  i + nums[i] > pt: pt = i + nums[i]

            if i == pt and not nums[i]: return False
            if pt >= len(nums)-1      : return True

        return True