class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        visit = [0]*n
        graph = defaultdict(list)
        st = []
        
        for u,v in edges:
            graph[u].append(v)
        
        def dfs(node):
            if visit[node]==1:
                return False
            if visit[node]==2:
                return True
            visit[node]=1
            for n in graph[node]:
                if not dfs(n):
                    return False
            visit[node]=2
            return True
        
        for i in range(len(visit)):
            if visit[i]==0:
               if not dfs(i):
                return False

        return True
            