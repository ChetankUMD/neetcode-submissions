class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        di = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0 
        dp=[[-1]*n for _ in range(m)]
        def dfs(r,c):
            if dp[r][c]!=-1:
                return dp[r][c]
            count=1
            for dr,dc in di:
                row ,col = r+dr,c+dc
                if 0 <= row < m and 0 <= col < n and mat[r][c]<mat[row][col]:
                    dp[r][c] = count=max(count,1+dfs(row,col))
            return count
        for i in range(m):
            for j in range(n):
                    res = max(res,dfs(i,j))
        return res
        
