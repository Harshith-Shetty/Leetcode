class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2: return True
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower(): return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper(): return False
        return True;
            