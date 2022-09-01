class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next_row = triangle[-1][:]
        curr_row = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + next_row[j]
                lower_right = triangle[i][j] + next_row[j + 1]
                curr_row[j] = min(lower_left, lower_right)

            curr_row, next_row = next_row, curr_row

        return next_row[0]