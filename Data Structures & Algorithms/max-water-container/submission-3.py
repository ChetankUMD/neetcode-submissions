class Solution:
    def maxArea(self, hs: List[int]) -> int:
        res = 0
        r = len(hs)-1
        l = 0

        while l<r:
            h = min(hs[l],hs[r])
            area = h * (r-l)
            res = max(res, area)
            if hs[l]>hs[r]:
                r-=1
            else:
                l+=1
        
        return res

