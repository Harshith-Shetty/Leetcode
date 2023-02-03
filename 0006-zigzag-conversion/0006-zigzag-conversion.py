class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = ['' for _ in range(numRows)]
        row = 0
        step = 1
        for c in s:
            zigzag[row] += c
            if row == numRows-1:
                step = -1
            elif row == 0:
                step = 1
            row += step
        return ''.join(zigzag)