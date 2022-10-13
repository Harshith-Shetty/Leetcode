class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mappings = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        def construct(idx=0, partial=[]):
            if idx >= len(digits):
                result.append(''.join(partial))
                return
            for ch in mappings[digits[idx]]:
                partial.append(ch)
                construct(idx+1, partial)
                partial.pop()

        construct()
        return result