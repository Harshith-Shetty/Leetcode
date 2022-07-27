class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        List =[]
        for x in range(numRows): # 0,1,2,3,4,5 --> n=6
            row_list = []
            for y in range(x+1): # 0,1,2,3,4 --> x =4 ; 5 elements / 5th row
                if(y == 0 or y == x):
                    row_list.append(1)
                else:
                    row_list.append(List[x-1][y-1]+List[x-1][y])
            List.append(row_list)
        return List
                