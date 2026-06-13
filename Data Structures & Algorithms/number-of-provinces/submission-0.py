class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = {}
        for m in range(len(isConnected)):
            l[m]=[]
            for n in range(len(isConnected[0])):
                if isConnected[m][n]==1:
                    l[m].append(n)
        visited = set()
        count = 0
        for i in range(len(l)):
            if i not in visited:
                count+=1
                self.dfs(i,l,visited)
        return count

    def dfs(self, node, l, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        for n in l[node]:
            if n not in visited:
                self.dfs(n, l, visited)
        return 
            