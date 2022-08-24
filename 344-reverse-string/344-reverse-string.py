class Solution:
    def reverseString(self, s: List[str]) -> None:
        for x in range(int(len(s)/2)):
            a = s[x]
            s[x] = s[((x+1)*-1)]
            s[((x+1)*-1)] = a
        return s
            
        