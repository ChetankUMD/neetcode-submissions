class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n = len(p)
        dp = [[-1]*2 for _ in range(n)]
        def dfs(ind, buy):
            if ind>=n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy] = max(-p[ind]+dfs(ind+1,0), dfs(ind+1,1))
            else:
                dp[ind][buy] = max(p[ind]+dfs(ind+2,1),dfs(ind+1,0))
            
            return dp[ind][buy]
        
        return dfs(0,1)