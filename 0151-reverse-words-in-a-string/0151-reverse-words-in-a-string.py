class Solution:
    def reverseWords(self, s: str) -> str:
        pt1 = len(s) -1
        result = []
        word = ""
        while pt1 > -1:
            if(s[pt1] == ' '):
                if(len(word) !=0):
                    result.append(word)
                    word =""
                
            else:
                word = s[pt1] + word
            pt1-=1
        if(len(word) != 0):
            result.append(word)
        return ' '.join(result)