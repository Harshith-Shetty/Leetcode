class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        i,j=0,1
        skip=0
        while i<N:
            if arr[i]!=j:
                skip+=1
                if skip==k:
                    return j
                j+=1    
            else:
                i+=1
                j+=1
        return arr[-1]+(k-skip)