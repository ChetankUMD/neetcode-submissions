class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        dp = [[-1]*n for _ in range(m)]
        def dfs(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp
            if s[i]==t[j]:
                return (dfs(i-1,j-1)+dfs(i-1,j))
            else:
                return dfs(i-1,j)
        
        return dfs(m-1,n-1)