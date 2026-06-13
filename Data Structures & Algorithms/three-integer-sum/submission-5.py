class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i<len(nums)-1:
            if i > 0 and nums[i] == nums[i - 1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1
            i+=1
        
        return res
        