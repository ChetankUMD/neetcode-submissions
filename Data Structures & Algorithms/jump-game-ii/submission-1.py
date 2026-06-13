class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        r=l=jumps=0
        while r < n-1:
            furtest = 0
            for i in range(l,r+1):
                furtest = max(furtest,i+nums[i])
            l=r+1
            r=furtest
            jumps+=1

        return jumps