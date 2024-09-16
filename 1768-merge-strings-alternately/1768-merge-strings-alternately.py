class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range (max(len(word1), len(word2))):
            if(i < len(word1)):
                result = result + word1[i]
            if(i < len(word2)):
                result = result + word2[i]
        return result