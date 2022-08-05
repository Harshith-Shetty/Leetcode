class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
        # output= []
        # length = len(nums)
        # nums.sort()
        # for x in range (length-2):
        #     i = x+1
        #     dict ={}
        #     while i<length:
        #         sum =0 - nums[i] - nums[x]
        #         if((sum)in dict):
        #             list = []
        #             list.append(nums[x])
        #             list.append(sum)
        #             list.append(nums[i])
        #             if(list in output):
        #                 pass
        #             else:
        #                 output.append(list)
        #         dict[nums[i]] = i
        #         i +=1
        # return output