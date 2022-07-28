class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        for x in range(n):
            if(freq[nums[x]] == 0):
                freq[nums[x]] += 1
            else:
                return nums[x]