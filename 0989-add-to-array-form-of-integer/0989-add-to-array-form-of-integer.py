class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ''.join(str(digit) for digit in num)
        res = [int(digit) for digit in str(int(num_str) + k)]
        return res
        