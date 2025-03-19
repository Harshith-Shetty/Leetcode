class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        #Bruteforce Approach
        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]