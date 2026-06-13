class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n+1)]
        def dfs(i,target):
            if target==0:
                return 1
            if i<0 or target<0:
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            
            dp[i][target] = dfs(i,target-coins[i]) + dfs(i-1,target)

            return dp[i][target]

        return dfs(n-1,amount)