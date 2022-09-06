class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1)
            
        count = Counter(nums1)
        ans = []
        for x in nums2:
            if count[x] > 0:
                ans.append(x)
                count[x] -= 1
        return ans
        