class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict = defaultdict(int)
        dict[0] =1
        output = 0
        Sum = 0
        for n in nums:
            Sum +=n
            m = Sum%k
            output += dict[m]
            dict[m]+=1
        return output
        
