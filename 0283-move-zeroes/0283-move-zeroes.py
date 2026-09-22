class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # without using a temp array
        index = 0

        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[index] = nums[curr]
                index +=1
            
        while index < len(nums):
            nums[index] = 0
            index +=1
        

        