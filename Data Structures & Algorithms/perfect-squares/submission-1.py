class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0]=0


        for target in range(1,n+1):
            for i in range(1, target+1):
                sq = i*i
                if target - sq < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target-sq])
        
        return dp[n]
        # def dfs(target):
        #     if target == 0:
        #         return 0
        #     if dp[target]!=-1:
        #         return dp[target]
        #     res = target
        #     for i in range(1, target):
        #         if i*i > target:
        #             break
        #         res = min(res, 1+dfs(target-(i*i)))
        #     dp[target]=res 
        #     return res
        
        # return dfs(n)