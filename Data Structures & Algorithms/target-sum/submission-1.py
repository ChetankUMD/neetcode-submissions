class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(i,result):
            if i==n:
                return 1 if result==0 else 0
            
            ways = dfs(i+1, result+nums[i])+dfs(i+1,result-nums[i])

            return ways
        
        return dfs(0,target)