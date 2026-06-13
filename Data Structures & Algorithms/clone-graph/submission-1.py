"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        oldtoNew = {}
        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]
            root = Node(node.val)
            oldtoNew[node]=root
            for n in node.neighbors:
                    root.neighbors.append(dfs(n))
            return root
        return dfs(node)