class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:
            return nums[0]
        dp= [-1]*(n+1)
        def dfs(i,total):
            if i > total:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]= max(nums[i]+dfs(i+2,total), dfs(i+1,total))
            return dp[i]
        ans1 = dfs(0,n-2)
        dp= [-1]*(n+1)
        ans2=dfs(1,n-1)
        return max(ans1,ans2)