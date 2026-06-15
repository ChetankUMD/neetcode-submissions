class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        l , r = 0, 1
        n = len(p)

        while r<n:
            res = max(res, (p[r]-p[l]))
            if p[l]>p[r]:
                l=r
            r+=1
        
        return res