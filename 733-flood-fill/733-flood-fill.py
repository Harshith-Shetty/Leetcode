class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h, w = len(image), len(image[0])
        def dfs( r, c, src_color, new_color): 
            if r < 0 or c < 0 or r >= h or c >= w or image[r][c] == new_color or image[r][c] != src_color:
                return
            image[r][c] = new_color
            dfs( r-1, c, src_color, new_color )
            dfs( r+1, c, src_color, new_color )
            dfs( r, c-1, src_color, new_color )
            dfs( r, c+1, src_color, new_color )
        dfs(sr, sc, src_color = image[sr][sc], new_color = color)
        return image
        