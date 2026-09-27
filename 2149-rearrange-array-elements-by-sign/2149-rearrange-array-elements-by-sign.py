class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [0]*len(nums)
        pos_index = 0
        neg_index = 1

        for i in nums:
            if(i < 0):
                temp[neg_index] = i
                neg_index +=2
            else:
                temp[pos_index] = i
                pos_index +=2
        return temp
        