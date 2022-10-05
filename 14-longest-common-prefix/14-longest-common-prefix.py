class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in zip(*strs):
            a = "".join(i)
            if len(set(a))!=1:
                return result
            else:
                result +=a[0]
        return result
                