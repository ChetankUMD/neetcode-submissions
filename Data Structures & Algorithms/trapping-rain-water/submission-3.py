class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        l = 0
        r = len(h)-1
        maxl = h[l]
        maxr =h[r]
        res = 0
        while l<r:
            if maxl <= maxr:
                l+=1
                maxl = max(maxl,h[l])
                res += maxl-h[l]
            else:
                r-=1
                maxr = max(maxr, h[r])
                res += maxr-h[r]
        return res