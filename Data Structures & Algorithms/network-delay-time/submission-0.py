class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        dist = [float("inf")]*(n+1)
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))

        heapq.heappush(heap,(0, k))
        dist[k]=0
        
        while heap:
            dis, node = heapq.heappop(heap)
            # print(heap)
            if dis > dist[node]:
                continue
            
            for nig_node, nig_dis in graph[node]:
                # print(nig_node)
                if dist[nig_node] > dis+nig_dis:
                    dist[nig_node]=dis+nig_dis
                    heapq.heappush(heap,(dist[nig_node], nig_node))
                    # print(heap)
        
        res = max(dist[1:])

        return -1 if res == float("inf") else res
