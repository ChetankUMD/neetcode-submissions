"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = {None: None}
        p = head
        while p:
            copy = Node(p.val)
            h[p] = copy
            p = p.next
        p = head
        while p:
            copy = h[p]
            copy.random = h[p.random]
            copy.next = h[p.next]
            p = p.next
        return h[head]
