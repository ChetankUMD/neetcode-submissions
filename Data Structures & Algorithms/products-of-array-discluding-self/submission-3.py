class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        p = 1
        post = [1] * len(nums) 
        po = 1

        for i in range(len(nums)):
            p = pre[i] = p *nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            po = post[i] = po * nums[i] 

        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = post[i+1]
            elif i == len(nums) -1:
                res[i] = pre[i-1]
            else:
                res[i] = pre[i-1] * post[i+1]
        
        return res