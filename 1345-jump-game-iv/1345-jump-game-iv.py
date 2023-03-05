class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for j, e in enumerate(arr):
            d[e].append(j)

        queue = deque([0])
        steps = 0
        visited = {0}
        n = len(arr)
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == n - 1:
                    return steps
                for e in [*d[arr[i]], i-1, i+1]:
                    if e not in visited and 0 <= e <= n:
                        visited.add(e)
                        queue.append(e)
                d[arr[i]].clear()
            steps += 1