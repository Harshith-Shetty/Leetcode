class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(S, step, curr, res):
            if step == len(s):
                res.append(curr)
                return
            if s[step].lower() == s[step].upper():
                backtrack(s, step+1, curr+s[step], res)
            else:
                backtrack(s, step+1, curr+s[step].lower(), res)
                backtrack(s, step+1, curr+s[step].upper(), res)
        res = []
        backtrack(s, 0, "", res)
        return res
        