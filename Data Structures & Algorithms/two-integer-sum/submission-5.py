class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in h:
                return [h[diff], i]
            else:
                h[nums[i]] = i

        return

        

        # low = 0
        # high = len(nums) -1

        # while low<high:
        #     sum = nums[low] + nums[high]

        #     if sum == target:
        #         return [low, high]
        #     elif sum > target:
        #         high -= 1
        #     else:
        #         low += 1
        
        # return []