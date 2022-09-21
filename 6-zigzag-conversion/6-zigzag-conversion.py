class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        row_arr = [""] * numRows
        row_idx = 1
        going_up = True

        for ch in s:
            row_arr[row_idx-1] += ch
            if row_idx == numRows:
                going_up = False
            elif row_idx == 1:
                going_up = True
            
            if going_up:
                row_idx += 1
            else:
                row_idx -= 1
        
        return "".join(row_arr)