class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ls=[]
        for i in range(n):
            ls+=[nums[i]]
            ls+=[nums[i+n]]
        return ls