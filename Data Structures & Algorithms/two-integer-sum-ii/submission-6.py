class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        while l<r:
            sum = nums[l]+nums[r]
            if sum == target:
                return [l+1,r+1]
            if sum > target:
                r-=1
            else:
                l+=1
            

        return