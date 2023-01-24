class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = collections.deque()
        n = len(board)
        queue.append((1, 0)) 
        visited = set()
        
        def square_to_idx(i):
            r, c = divmod(i - 1, n)
            if r % 2 != 0:
                c = n - c - 1
            r = n - r - 1
            return r, c
        
        while queue:
            cur_val, path_len = queue.popleft()
            visited.add(cur_val)
            cur_row, cur_col = square_to_idx(cur_val)
            if board[cur_row][cur_col] != -1:
                cur_val = board[cur_row][cur_col]
            if cur_val == n ** 2:
                return path_len
            max_move = min(cur_val + 6, n ** 2)
            for dest_val in range(cur_val + 1, max_move + 1):
                if dest_val not in visited:
                    queue.append((dest_val, path_len + 1))

        return -1