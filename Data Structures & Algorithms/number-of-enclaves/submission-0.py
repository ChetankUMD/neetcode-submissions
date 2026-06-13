class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        m,n = len(board), len(board[0])
        v = [[0 for _ in range(n)] for _ in range(m)]
        dic = [[-1,0],[0,1],[1,0],[0,-1]]

        def dfs(r,c):        
            if (r < 0 or c < 0 or r >= m or
                    c >= n or board[r][c]==0 or v[r][c]==1
                ):
                    return 0
            v[r][c]=1
            for dr, dc in dic:
                row = dr+r
                col = dc+c
                dfs(row,col)
            return

        for j in range(n):
            if v[0][j]!=1 and board[0][j]==1:
                dfs(0,j)
        
        for i in range(1,m-1):
            if v[i][n-1]!=1 and board[i][n-1]==1:
                dfs(i,n-1)
        
        if m > 1:
            for i in range(n-1,-1,-1):
                if v[m-1][i]!=1 and board[m-1][i]==1:
                    dfs(m-1,i)
        
        if n>1:
            for i in range(m-2,0,-1):
                if v[i][0]!=1 and board[i][0]==1:
                    dfs(i,0)
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]==1 and v[i][j]!=1:
                    count+=1
        
        return count