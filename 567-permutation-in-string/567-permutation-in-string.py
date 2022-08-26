class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count =  [0]*26
        s2count =  [0]*26
        
        for i in range(len(s1)):
            s1count[ord(s1[i])-97] += 1
            s2count[ord(s2[i])-97] += 1 
            
        if s1count == s2count:
            return True
        
        for i in range(len(s1),len(s2)):
            
            s2count[ord(s2[i])-97] += 1
            s2count[ord(s2[i-len(s1)])-97] -= 1
            
            if s1count == s2count:
                return True
        
        return False