class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        m , n = len(grid), len(grid[0])
        res = 0

        def dfs(r,c, count):
            if (r < 0 or c < 0 or r >= m or
                    c >= n or grid[r][c]==0
                ):
                    return 0
            count =1
            grid[r][c]=0
            for dr,dc in dic:
                count = count+dfs(dr+r,dc+c, count)
            return count
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count =0
                    res = max(res, dfs(i,j, count))

        return res