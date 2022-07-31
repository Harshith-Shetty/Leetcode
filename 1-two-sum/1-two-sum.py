class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        output = []
        for x,y in enumerate(nums):
            if(target-y in dict):
                output.append(dict[target-y])
                output.append(x)
                return output
            else:
                dict[y] = x
        