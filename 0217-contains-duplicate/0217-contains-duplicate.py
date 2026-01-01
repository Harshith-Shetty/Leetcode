class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Using set
        if(len(set(nums)) != len(nums)):
            return True
        return False