class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def combinations(idx, curArr, nums, res):
            if len(curArr) >= 2:
                res.add(curArr)
            for i in range(idx, len(nums)):
                if not curArr or nums[i] >= curArr[-1]:
                    combinations(i+1, curArr+(nums[i],), nums, res)

        res = set()
        combinations(0, (), nums, res)
        return res