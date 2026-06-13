class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        l = {}
        m,n = len(grid), len(grid[0])
        v = [[0 for _ in range(n)] for _ in range(m)]
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        s = set()
        def dfs(r,c,rootRow, rootCol,a):
            if (r < 0 or c < 0 or r >= m or
                    c >= n or grid[r][c]==0 or v[r][c]==1
                ):
                    return
            v[r][c]=1
            a.append((r-rootRow,c-rootCol))
            for dr, dc in dic:
                row = dr+r
                col = dc+c
                dfs(row,col,rootRow,rootCol,a)
            return a

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and v[i][j]!=1:
                    a=[]
                    s.add(tuple(dfs(i,j,i,j,a)))
        
        return len(s)

    