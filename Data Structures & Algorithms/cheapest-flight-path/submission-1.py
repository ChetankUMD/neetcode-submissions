class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for s,d,p in flights:
            graph[s].append((d,p))
        print(graph)
        heap = []
        heapq.heappush(heap,(0,src,0))
        price = [float("inf")] * n
        while heap:
            cur_stops, cur_node, cur_price = heapq.heappop(heap)
            if cur_stops>k:
                continue
            for next_node, next_price in graph[cur_node]:
                if price[next_node] > cur_price+next_price:
                    price[next_node]=cur_price+next_price
                    heapq.heappush(heap,(cur_stops+1,next_node,price[next_node]))
                    print(heap)
        return price[dst] if price[dst] != float("inf") else -1

