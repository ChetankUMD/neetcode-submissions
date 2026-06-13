class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        res = float("-inf")
        sum = 0
        for i in range(n):
            sum +=nums[i]
            res = max(res, sum)
            if sum <0:
                sum=0
            
        
        return res