class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        def dfs(i, prev_i):
            if i==n:
                return 0
            if dp[i][prev_i+1] != -1:
                return dp[i][prev_i+1]

            not_take = dfs(i+1,prev_i)
            take = 0
            if prev_i == -1 or nums[i]>nums[prev_i]:
                take = 1+dfs(i+1,i)
            dp[i][prev_i+1]=max(not_take,take)
            return dp[i][prev_i+1]
        
        return dfs(0,-1)

            