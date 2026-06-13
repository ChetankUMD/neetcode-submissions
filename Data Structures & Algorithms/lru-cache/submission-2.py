class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt , prev

    def add(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev, node.next = prev, self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        res = 0
        if key in self.cache:
            res = self.cache[key]
            self.remove(res)
            self.add(res)
            return res.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] =Node(key, value)
        self.add(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
