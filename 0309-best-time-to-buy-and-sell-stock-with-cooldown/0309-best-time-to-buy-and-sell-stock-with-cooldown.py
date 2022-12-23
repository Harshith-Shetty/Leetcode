class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 0
        for x in range(1,len(prices)):
            temp = p1
            p1 = max(p1+prices[x]-prices[x-1], p2)
            p2 = max(temp, p2)
        return max(p1,p2)