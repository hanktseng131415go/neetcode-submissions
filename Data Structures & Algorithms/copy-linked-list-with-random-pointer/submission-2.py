"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # recursion
        if not head:
            return None
        if head in self.map:
            return self.map[head]

        copy = Node(head.val)
        self.map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)

        return copy

        # # hash map, one pass:
        # # time: n 
        # # space: n
        # from collections import defaultdict

        # h_map = defaultdict(lambda: Node(0))
        # h_map[None] = None
        # cur = head
        # while cur:
        #     h_map[cur].val = cur.val
        #     h_map[cur].next = h_map[cur.next]
        #     h_map[cur].random = h_map[cur.random]
        #     cur = cur.next
        
        # return h_map[head]

        # # hash_map, two pass:
        # # time: n
        # # space: n 
        # h_map = {None:None}
        # cur = head
        # while cur:
        #     copy_node = Node(cur.val)
        #     h_map[cur] = copy_node
        #     cur = cur.next
        
        # cur = head
        # while cur:
        #     copy = h_map[cur]
        #     copy.next = h_map[cur.next]
        #     copy.random = h_map[cur.random]
        #     cur = cur.next
        
        # return h_map[head]