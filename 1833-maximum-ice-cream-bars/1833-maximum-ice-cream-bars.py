class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result=0
        costs.sort()
        for i in costs:
            if coins<i:
                break
            result+=1
            coins-=i
        return result
        