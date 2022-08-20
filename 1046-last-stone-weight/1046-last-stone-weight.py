class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stones.sort()
            if len(stones)>2:
                if stones[-1]==stones[-2]:
                    del stones[-1]
                    del stones[-1]
                elif stones[-1]>stones[-2]:
                    stones[-1]-=stones[-2]
                    del stones[-2]
            else:
                return stones[-1]-stones[-2]        
        return stones[0]
        