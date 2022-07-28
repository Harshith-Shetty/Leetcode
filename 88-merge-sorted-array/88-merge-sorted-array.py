class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in range(len(nums2)):
            nums1[-1-x]=nums2[x]
        nums1.sort(key = lambda x:x)
        return nums1
    