class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        acc = list(accumulate([0] + sorted(costs)))
        count = bisect_left(acc, coins)
        try: return count if acc[count] == coins else count - 1
        except IndexError: return count - 1
        