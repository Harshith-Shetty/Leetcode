class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        for x,g in groupby(nums):
            t=len(list(g))
            
            if x==0:
                res+=comb(t+1,2)
        return res