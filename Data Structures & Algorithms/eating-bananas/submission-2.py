class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res = float('inf')

        while l<=r:
            mid = (l+r)//2
            max_ba=0
            for n in piles:
                max_ba += math.ceil(n/mid)
            if max_ba > h:
                l=mid+1
            else:
                res = mid
                r=mid-1
        
        return res