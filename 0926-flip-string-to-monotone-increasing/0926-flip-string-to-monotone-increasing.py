class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num_flips = 0
        num_ones = 0
        
        for num in s:
            # If it is one, imagine we are adding it to the end. Therefor it is always satisfying monotonicity
            if num =='1':
                num_ones += 1
            # Otherwise, we need to flip the 0, so increment flips. If after that, we have more flips than ones,
            # flip the ones instead. Do this by setting num_flips to num_ones
            else:
                num_flips += 1
                if num_flips > num_ones:
                    num_flips = num_ones
                    
        return num_flips