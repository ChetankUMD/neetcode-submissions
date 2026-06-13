class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n-1 edges
        if len(edges)!=n-1:
            return False
        # create a graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        # no cycle
        visit = [0]*n
        q = deque()
        q.append(0)

        # Can be reached in one dfs
        while q:
            node = q.popleft()
            visit[node] = 1
            for nig in graph[node]:
                if visit[nig]==1:
                    continue
                q.append(nig)

        for v in visit:
            if v == 0:
                return False
        
        return True


























        # st = set()
        # graph = defaultdict(list)
        # if len(edges)!=n-1:
        #     return False
        # for i in range(len(edges)):
        #     graph[edges[i][0]].append(edges[i][1])
        #     graph[edges[i][1]].append(edges[i][0])
        
        # def dfs(node,parent):
        #     st.add(node)
        #     for n in graph[node]:
        #         if n == parent:
        #             continue
        #         if n in st:
        #             return False
        #         if not dfs(n, node):
        #             return False
        #     return True
        
        
        # if not dfs(0,-1):
        #     print(st)
        #     return False
        
        # return len(st)==n