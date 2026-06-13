class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}

        for n in nums:
            if n in h:
                h[n] +=1
            else:
                h[n] = 1

            if h[n] > 1:
                return True

        return False