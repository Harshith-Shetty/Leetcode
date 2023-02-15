class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ''.join(map(str, num))
        result = int(num_str) + k
        return list(map(int, str(result)))