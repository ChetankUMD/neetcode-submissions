class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1),len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                ways = float("inf")
                if word1[i-1]==word2[j-1]:
                    ways = dp[i-1][j-1]
                else:
                    ways = min(ways,1+dp[i-1][j],1+dp[i][j-1],1+dp[i-1][j-1])
                dp[i][j]=ways
        print(dp)
        return dp[m][n]

        # def dfs(i,j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     ways = float("inf")
        #     if word1[i]==word2[j]:
        #         ways = dfs(i-1,j-1)
        #     else:
        #         ways = min(ways,1+dfs(i-1,j),1+dfs(i,j-1),1+dfs(i-1,j-1))
        #     dp[i][j]=ways
        #     return ways
        
        # return dfs(m-1,n-1)

        [[0, 1, 2, 3, 4, 5], 
        [1, -1, -1, -1, -1, -1], 
        [2, -1, -1, -1, -1, -1], 
        [3, -1, -1, -1, -1, -1], 
        [4, -1, -1, -1, -1, -1], 
        [5, -1, -1, -1, -1, -1], 
        [6, -1, -1, -1, -1, -1], 
        [7, -1, -1, -1, -1, -1]]

        [[0, 1, 2, 3, 4, 5],
        [1, 0, 1, 2, 3, 4],
        [2, 1, 0, 1, 2, 3], 
        [3, 2, 1, 0, 1, 2], 
        [4, 3, 2, 1, 1, 2], 
        [5, 4, 3, 2, 1, 2], 
        [6, 5, 4, 3, 2, 1], 
        [7, 6, 5, 4, 3, 2]]