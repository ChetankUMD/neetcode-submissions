class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        s = set(nums)
        res = 0
        for n in nums:
            if n-1 in h:
                continue
            count = 1
            while n + 1 in s:
                h[n] = 1
                count += 1
                n = n+1
            
            res = max(count, res)
        return res

        # s = set(nums)
        # res = 0
        # for n in s:
        #     count = 1
        #     while n + 1 in s:
        #         count += 1
        #         n = n+1
            
        #     res = max(count, res)

        # return res