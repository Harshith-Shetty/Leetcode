class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        curr = [[nums[0]]]
        for x in nums[1:]:
            curr += [y+[x] for y in curr if x>=y[-1]]
            curr += [[x]]
        curr = [tuple(x) for x in curr if len(x)>=2]
        return list(set(curr))