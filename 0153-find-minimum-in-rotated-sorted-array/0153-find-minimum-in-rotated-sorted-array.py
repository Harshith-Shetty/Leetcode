class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < s:
                return nums[i]
            s = nums[i]
        return nums[0]