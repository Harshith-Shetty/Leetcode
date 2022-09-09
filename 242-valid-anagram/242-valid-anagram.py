class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for ele in s:
            if ele not in dict:
                dict[ele] = 1
            else:
                dict[ele] += 1
        for ele in t:
            if ele not in dict:
                return False
            else:
                dict[ele] -= 1
        return False if any(dict.values()) else True