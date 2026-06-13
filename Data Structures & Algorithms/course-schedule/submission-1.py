class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        visit = [0]*n
        graph = defaultdict(list)
        indegree = [0]*n
        q = deque()
        
        count=0
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            count+=1
            for ni in graph[node]:
                indegree[ni]-=1
                if indegree[ni]==0:
                    q.append(ni)

        if count!=n:
            return False

        return True
