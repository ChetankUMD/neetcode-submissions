class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(len(points)):
                if i==j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((j,dist))
        
        mst = []
        visit = [0]* len(points)
        heap=[]
        res = 0
        #(dist,node,parent)
        heapq.heappush(heap,(0,0,-1))

        while heap:
            cur_dist, cur_node, cur_par = heapq.heappop(heap)
            if visit[cur_node]==1:
                continue
            visit[cur_node]=1
            if cur_node != 0:
                mst.append((cur_node,cur_par))
            res = res+cur_dist
            for next_node, next_dist in graph[cur_node]:
                heapq.heappush(heap,(next_dist,next_node,cur_node))


        return res