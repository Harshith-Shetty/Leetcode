class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval = 0
        result = []
        for i in candies:
            if(i > maxval):
                maxval = i
                
        for i in candies:
            if(i+extraCandies < maxval):
                result.append(False)
            else:
                result.append(True)
        return result
            
        