class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))            
        w1 = list(word1)
        w2 = list(word2)        
        num = 0
        queue = deque()
        queue.append((0, 0))
        visited = set()
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                    i += 1
                    j += 1
                if i == len(w1) and j == len(w2):
                    return num
                queue.append((i, j + 1))
                queue.append((i + 1, j + 1))
                queue.append((i + 1, j))
            num += 1