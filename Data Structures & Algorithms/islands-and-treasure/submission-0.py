class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        INF = 2147483647
        level = 0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        
        while q:
            r, c = q.popleft()
            for dr,dc in dic:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c] + 1:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            level+=1
    
        
        return

            