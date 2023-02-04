class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L=len(s1)
        dic_s2={}
        dic_s1={}
        l=0
        for char in set(s1+s2):
            dic_s2[char]=0
            dic_s1[char]=0
        for char in s1:
            dic_s1[char]+=1
        if len(s2)<L:
            return False
        for i in range(L):
            dic_s2[s2[i]]+=1
        if dic_s2==dic_s1:
                return True
        for i in range(L,len(s2)):
            dic_s2[s2[l]]-=1
            l+=1
            dic_s2[s2[i]]+=1
            if dic_s2==dic_s1:
                return True 
        return False