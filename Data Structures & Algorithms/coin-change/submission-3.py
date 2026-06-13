class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        res = float("inf")
        dp = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in dp:
                return dp[rem]
            ans = float('inf')
            for coin in coins:
                dp[rem] = ans = min(ans, 1 + dfs(rem - coin))

            return ans
        res = dfs(amount)
        return res if res != float("inf") else -1