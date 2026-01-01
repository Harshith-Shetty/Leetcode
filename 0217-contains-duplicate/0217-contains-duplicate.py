class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Using Maps
        mpp ={}
        for i in range(len(nums)):
            if nums[i] in mpp:
                return True
            mpp[nums[i]] = 1
        return False