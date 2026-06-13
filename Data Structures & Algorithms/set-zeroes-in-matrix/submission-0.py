class Solution:
    def setZeroes(self, ma: List[List[int]]) -> None:
        zero = []
        m = len(ma)
        n = len(ma[0])
        for i in range(m):
            for j in range(n):
                if ma[i][j] == 0:
                    zero.append([i, j])

        for r in zero:
            for i in range(n):
                ma[r[0]][i] = 0
        
        for c in zero:
            for j in range(m):
                ma[j][c[1]] = 0

        