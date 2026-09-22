class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # using temp list O(n)
        temp = [0] * len(nums)
        index = 0
        curr = 0

        while curr < len(nums):
            if nums[curr] != 0:
                temp[index] = nums[curr]
                index +=1
            curr +=1
        nums[:] = temp

        