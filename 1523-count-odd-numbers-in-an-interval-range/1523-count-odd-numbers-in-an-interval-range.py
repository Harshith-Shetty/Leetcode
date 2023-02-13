class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=(high-low+1)//2
        if(low&1 and high&1):
            return a+1 
        return a