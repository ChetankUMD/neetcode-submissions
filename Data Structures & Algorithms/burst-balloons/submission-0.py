class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums =[1]+nums+[1]
        dp = {}
        
        def dfs(i,j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=0
            for k in range(i,j+1):
                cost = nums[i-1]*nums[k]*nums[j+1]+dfs(i,k-1)+dfs(k+1,j)
                dp[(i,j)] = max(dp[(i,j)],cost)
        
            return dp[(i,j)]

        return dfs(1,len(nums)-2)
        
