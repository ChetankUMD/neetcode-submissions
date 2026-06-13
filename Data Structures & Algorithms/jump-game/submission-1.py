class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0

        for i in range(len(nums)):
            if max_i >=len(nums)-1:
                return True
            max_i = max(max_i, i+nums[i])
            if max_i <= i:
                return False
            
        
        return