class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        st = set()
        graph = defaultdict(list)
        if len(edges)!=n-1:
            return False
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        def dfs(node,parent):
            st.add(node)
            for n in graph[node]:
                if n == parent:
                    continue
                if n in st:
                    return False
                if not dfs(n, node):
                    return False
            return True
        
        
        if not dfs(0,-1):
            return False
        return len(st)==n