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
        h_map = {None:None}
        cur = head
        while cur:
            copy_node = Node(cur.val)
            h_map[cur] = copy_node
            cur = cur.next
        
        cur = head
        while cur:
            copy = h_map[cur]
            copy.next = h_map[cur.next]
            copy.random = h_map[cur.random]
            cur = cur.next
        
        return h_map[head]