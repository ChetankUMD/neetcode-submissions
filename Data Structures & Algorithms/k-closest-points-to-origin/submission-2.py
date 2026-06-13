import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x1, y1 in points:
            dist = math.sqrt(x1**2 +y1**2)
            heapq.heappush(minheap, (dist,x1,y1))
        print(minheap)
        res = []
        for _ in range(k):
            _, x,y=heapq.heappop(minheap)
            print(x)
            print(y)
            res.append([x,y])
        
        return res