class Node:

    def __init__(self, key, val, nxt=None, pre=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.pre = self.left
        self.cap = capacity

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
        
    def remove(self, node):
        pre, nxt = node.pre, node.nxt
        pre.nxt = nxt
        nxt.pre = pre

    def insert(self, node):
        pre, nxt = self.right.pre, self.right
        pre.nxt, nxt.pre = node, node
        node.pre = pre
        node.nxt = nxt

