class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n =len(nums)
        max_res = float("-inf")
        prefix = 1
        sufix = 1
        for i in range(n):
            if prefix == 0: prefix=1
            if sufix == 0: sufix =1
            prefix = prefix*nums[i]
            sufix = sufix*nums[n-i-1]
            max_res = max(max_res,prefix,sufix)
    
        return max_res