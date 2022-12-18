class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            t = temperatures[i]
            while stack != [] and temperatures[stack[-1]] < t:
                less_index = stack.pop()
                res[less_index] = i - less_index
            stack.append(i)
        return res