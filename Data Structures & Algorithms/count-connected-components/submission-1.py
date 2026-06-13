class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        visit = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        def dfs(node):
            visit[node]=1
            for n in graph[node]:
                if visit[n]==0:
                    dfs(n)
            return

        for i in range(n):
            if visit[i]==0:
                count+=1
                dfs(i)
            
        return count