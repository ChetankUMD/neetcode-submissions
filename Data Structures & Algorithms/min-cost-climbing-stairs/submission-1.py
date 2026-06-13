class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        def dfs(i):
            if i >= n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            left = dfs(i+1)+cost[i]
            right = dfs(i+2)+cost[i]
            dp[i]=min(left, right)
            return dp[i]


        return min(dfs(0),dfs(1))       