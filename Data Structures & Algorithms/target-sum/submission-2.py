class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i,result):
            if i==n:
                return 1 if result==0 else 0
            if (i, result) in dp:
                return dp[(i, result)]
            dp[(i, result)] = dfs(i+1, result+nums[i])+dfs(i+1,result-nums[i])

            return dp[(i, result)]
        
        return dfs(0,target)