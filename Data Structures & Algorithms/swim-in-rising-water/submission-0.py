class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        m,n = len(grid), len(grid[0])
        dic = [[-1,0],[0,1],[1,0],[0,-1]]
        heapq.heappush(heap, (grid[0][0],0,0))
        print(heap)
        visit = [[0 for _ in range(n)] for _ in range(m)]
        visit[0][0]=1
        while heap:
            max_time, cur_row, cur_col = heapq.heappop(heap)
            visit[cur_row][cur_col]=1
            if cur_row==m-1 and cur_col ==n-1:
                return max_time
            for dr, dc in dic:
                row, col = dr+cur_row, dc+cur_col
                if 0 <= row < m and 0 <= col < n and visit[row][col]!=1:
                    heapq.heappush(heap,(max(max_time, grid[row][col]), row, col))

        return 0
