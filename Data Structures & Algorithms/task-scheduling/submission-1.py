class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        h = {}
        for s in tasks:
            h[s]=h.get(s,0)+1
        for _,v in h.items():
            heapq.heappush(maxheap, -v)

        q = deque()
        time = 0

        while maxheap or q:
            time = time+1
            if q and q[0][1]== time:
                num, t = q.popleft()
                heapq.heappush(maxheap, num)
            print(q)
            if maxheap:
                count = heapq.heappop(maxheap)
                count = count+1
                if count<0:
                    q.append((count,time+n+1))
        
        return time
                
