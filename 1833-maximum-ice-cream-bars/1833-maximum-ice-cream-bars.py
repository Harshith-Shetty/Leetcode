class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result=0
        costs.sort()
        for x,y in enumerate(costs):
            if coins<y:
                break
            result+=1
            coins -=y
        return result
        