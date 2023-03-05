class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        dict = collections.defaultdict(list)
        for i , n in enumerate(arr): dict[n].append(i)

        N = len(arr)        
        visited = {0, N - 1}
        s1, s2 = {0}, {N - 1}
        step = 0
        while s1:
            if len(s1) > len(s2): s1, s2 = s2, s1

            s3 = set()
            while s1:
                i = s1.pop()
                for n in [i - 1, i + 1] + dict[arr[i]]:
                    if n in s2: return step + 1
                    if n in visited: continue
                    if not 0 <= n < N: continue
                    visited.add(n)
                    s3.add(n)
                del dict[arr[i]]

            s1 = s3
            if s1: step = step + 1
        return -1