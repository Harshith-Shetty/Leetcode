class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = list(range(26))
        def find(c):
            return c if ds[c] == c else find(ds[c])
        for i in range(len(s1)):
            c_1, c_2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            p_1, p_2 = find(c_1), find(c_2)
            if p_1 != p_2:
                ds[max(p_1, p_2)] = min(p_1, p_2)
        answer = ""
        for c in baseStr:
            answer += chr(find(ord(c) - ord('a')) + ord('a'))
        return answer