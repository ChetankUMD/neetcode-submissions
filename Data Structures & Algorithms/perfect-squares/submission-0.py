class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1]*(n+1)
        def dfs(target):
            if target == 0:
                return 0
            if dp[target]!=-1:
                return dp[target]
            res = target
            for i in range(1, target):
                if i*i > target:
                    break
                res = min(res, 1+dfs(target-(i*i)))
            dp[target]=res 
            return res
        
        return dfs(n)