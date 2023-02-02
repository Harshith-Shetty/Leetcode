class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        i = 0
        for letter in order:
            dict[letter] = i
            i+=1
        x = 0
        first, second = 0, 1
        while second < len(words):
            idx = 0
            f = words[first]
            s = words[second]
            print(f, s)
            while idx < min(len(f), len(s)):
                
                if dict[f[idx]] > dict[s[idx]]:
                    return False
                elif dict[f[idx]] < dict[s[idx]]:
                    x = 1
                    break
                idx += 1
            if x == 0 and idx < max(len(f),len(s)) and len(f)>len(s):
                return False

            first += 1 
            second += 1
            
        return True