class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for num in nums:
            h[num] = h.get(num, 0) + 1
        
        # heap = []
        # for key,value in h.items():
        #     heapq.heappush(heap, [value,key])
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        print(h)
        sorted_h = sorted(h.items(), key=lambda x:x[1], reverse=True)

        res = []
        print(sorted_h)
        # while heap:
        #     res.append(heapq.heappop(heap)[1])
        for l in sorted_h:
            if k != 0:
                res.append(l[0])
            else:
                break
            k-=1

        return res