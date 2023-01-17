class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cost = 0
        for x in s:
            if x=='0':
                cost += 1
        output = cost
        for x in s: 
            if x=='0':
                cost -= 1 
            else:
                cost += 1
            output = min(output,cost)
        return output