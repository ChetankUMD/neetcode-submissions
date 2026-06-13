class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n= len(grid), len(grid[0])
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        count = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= m or
                    c >= n or grid[r][c] == "0"
                ):
                    return
            grid[r][c] = "0"
            for dr, dc in dic:
                dfs(r+dr, c+dc)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
            
        return count
