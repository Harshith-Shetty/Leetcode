class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            longest = max(longest, cur_longest)
        return longest