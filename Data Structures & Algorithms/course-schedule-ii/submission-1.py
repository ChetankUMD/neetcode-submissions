class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        visit = [0]*n
        graph = defaultdict(list)
        indegree = [0]*n
        q = deque()
        
        topo=deque()
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                topo.append(i)
        print(topo)
        while q:
            node = q.popleft()
            for ni in graph[node]:
                indegree[ni]-=1
                if indegree[ni]==0:
                    q.append(ni)
                    topo.appendleft(ni)
        if len(topo) != n:
            return []
        return list(topo)