class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        for i in range(len(nums)-1, -1,-1):
            swap = False 
            for j in range(i):
                if(nums[j] > nums [j + 1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if swap == False:
                break
        return nums
        