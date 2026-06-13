# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if root is None:
            return 0
        def dfs(root, maxValue):
            if root is None:
                return
            if root.val >= maxValue:
                self.res+=1
            maxValue = max(root.val, maxValue)
            dfs(root.left, maxValue)
            dfs(root.right, maxValue)
            return

        n=float("-inf")
        dfs(root, n)

        return self.res

    

