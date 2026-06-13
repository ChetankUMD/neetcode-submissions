class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n =len(nums)
        res = nums[0]
        for i in range(n):
            product =nums[i]
            res = max(res, product)
            for j in range(i+1, n):
                product *=nums[j]
                res = max(res, product)
        return res