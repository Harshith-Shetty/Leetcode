class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        current_capital = w
        i = 0
        available_projects = []
        while k:
            while i < n and projects[i][0] <= current_capital:
                heapq.heappush(available_projects, -projects[i][1])
                i += 1

            if available_projects:
                current_capital += -heapq.heappop(available_projects)
            k -= 1
        return current_capital