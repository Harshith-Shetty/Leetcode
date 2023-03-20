class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newArr=[0]+flowerbed+[0]
        count=0
        for i in range(0,len(newArr)):
            if newArr[i:i+3]==[0,0,0]:
                count+=1
                newArr[i+1]=1
                
        return count>=n     