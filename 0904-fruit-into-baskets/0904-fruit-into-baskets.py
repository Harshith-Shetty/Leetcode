class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if len(Counter(fruits))<3:
            return n

        dic = defaultdict(int)
        res,st = 0,0
        for end in range(n):
            dic[fruits[end]]+=1
            while len(dic)>2:
                dic[fruits[st]]-=1
                if dic[fruits[st]]==0:
                    del dic[fruits[st]]
                st+=1
            res = max(res,end-st+1)

        return max(res,n-st)

