class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[none_zero], nums[i] = nums[i], nums[none_zero]
                none_zero += 1