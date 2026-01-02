class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        
        counter = [0]*26

        for i in s:
            counter[ord(i)-ord('a')] +=1

        for j in t:
            counter[ord(j)-ord('a')] -=1
        
        for m in counter:
            if(m != 0):
                return False
        return True