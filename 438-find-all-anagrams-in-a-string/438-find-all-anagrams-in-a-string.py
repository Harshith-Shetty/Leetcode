class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        LS, LP, S, P, A = len(s), len(p), 0, 0, []
        if LP > LS: 
            return []
        for i in range(LP): S, P = S + hash(s[i]), P + hash(p[i])
        if S == P: A.append(0)
        for i in range(LP, LS):
            S += hash(s[i]) - hash(s[i-LP])
            if S == P: A.append(i-LP+1)
        return A