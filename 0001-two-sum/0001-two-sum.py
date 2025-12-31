class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mpp = {}
        
        for i in range(len(nums)):
            if(target - nums[i] in mpp ):
                return[mpp[target - nums[i]],i]
            mpp[nums[i]] = i