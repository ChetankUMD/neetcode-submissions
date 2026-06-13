class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        res = float("-inf")
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum +=nums[j]
                res = max(res,sum)
        
        return res