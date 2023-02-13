class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=(high-low+1)//2
        return a+1 if(low&1 and high&1) else a