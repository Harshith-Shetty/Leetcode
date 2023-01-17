class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        result = 0
        ones = 0
        
        for num in s:
            if num =='1':
                ones += 1
            else:
                result += 1
                if result > ones:
                    result = ones
                    
        return result