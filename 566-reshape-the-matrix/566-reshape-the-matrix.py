class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        output = []
        matrix = []

        for sublist in mat:
            for item in sublist:
                output.append(item)

        if len(output) != r * c:
            return mat
        else:
            for i in range(0,len(output),c):
                matrix.append(output[i:i+c])
            return matrix
        