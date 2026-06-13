class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        m , n= len(image), len(image[0])
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        pixel = image[sr][sc]
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= m or
                    c >= n or image[r][c]!=pixel
                ):
                    return
            image[r][c]=color
            for dr,dc in dic:
                    dfs(dr+r,dc+c)
        
        dfs(sr, sc)
        return image