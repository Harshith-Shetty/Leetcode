class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        cnts={}
        index=0
        min_value,max_value=min(nums),max(nums)
        for i in nums:
            cnts[i]=cnts.get(i,0)+1
        for i in range(min_value,max_value+1):
            while cnts.get(i,0)>0:
                nums[index]=i
                index+=1
                cnts[i]-=1
        return nums