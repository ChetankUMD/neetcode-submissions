class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        result = 0
        while l<=r:
            mid = l + (r-l) // 2
            if self.countHours(piles, h, mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result


    def countHours(self, piles: List[int], h: int, k: int) -> bool:
        count = 0
        for n in piles:
            count += math.ceil(n/k)
            if count > h:
                return False
        return True