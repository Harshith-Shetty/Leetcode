class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for idx, char in enumerate(order):
            dic[char] = idx
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if dic[words[i][j]] > dic[words[i+1][j]]:
                        return False
                    break

        return True