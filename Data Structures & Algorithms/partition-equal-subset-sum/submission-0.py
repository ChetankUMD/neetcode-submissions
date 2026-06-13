class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = 0
        for nu in nums:
            total += nu
        if total%2 !=0:
            return False
        target = total//2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        def dfs(i, add):
            if add==0:
                return True
            if i>=n or add<0:
                return False
            if memo[i][add] != -1:
                return memo[i][add]

            memo[i][add] = dfs(i+1,add) or dfs(i+1, add-nums[i])

            return memo[i][add]
    
        return dfs(0,target) 