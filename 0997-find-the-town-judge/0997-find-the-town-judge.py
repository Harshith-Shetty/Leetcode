class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={i:[] for i in range(1,n+1)}    
        for i in trust:
            d[i[0]].append(i[1])        
        output=-1
        for k,v in d.items():
            if len(v)==0:
                output=k 
                break 
        if output==-1:
            return -1
        for k,v in d.items():
            if output not in v and output!=k:
                return -1
        return output