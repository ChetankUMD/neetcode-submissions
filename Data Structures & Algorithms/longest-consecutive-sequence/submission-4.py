class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            count = 1
            while n + 1 in s:
                count += 1
                n = n+1
            
            res = max(count, res)

        return res