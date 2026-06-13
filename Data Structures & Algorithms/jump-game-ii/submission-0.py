class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i>=n-1:
                return 0
            min_jump = float("inf")
            for ind in range(i+1, min(n, i + nums[i] + 1)):
                min_jump = min(min_jump, 1+dfs(ind))
            
            return min_jump  
        
        return dfs(0)