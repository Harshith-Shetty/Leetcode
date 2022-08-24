class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()                  
        output = []
        for word in s:                         
            i = 0
            j = (len(word) - 1)
            while (i < j):
                word = list(word)
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            a = (''.join(word))
            output.append(a)
        return(' '.join(output))
                    
        