class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            heapq.heappush(heap, [c, n])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        # freq = [[] for i in range(len(nums)+1)]
        # count = {}
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        
        # for n, c in count.items():
        #     freq[c].append(n)
        
        # res = []
        # print(freq)
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        # return res
        