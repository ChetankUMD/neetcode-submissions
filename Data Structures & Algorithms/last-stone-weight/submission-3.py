class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for n in stones:
            heapq.heappush(maxheap, -n)

        while len(maxheap)>1:
            s1 = -heapq.heappop(maxheap)
            s2 = -heapq.heappop(maxheap)
            if s1-s2 ==0:
                continue
            heapq.heappush(maxheap,-(s1-s2))
            print(maxheap)
        res = 0
        maxheap.append(0)
        return abs(maxheap[0])