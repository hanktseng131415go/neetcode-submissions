# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Iteration - I

        def reverse(head):

            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            return prev

        dummy = ListNode(0, head)
        lp = dummy
        for _ in range(left - 1):
            lp = lp.next

        cur = lp.next
        tail = cur
        for _ in range(right - left):
            tail = tail.next
        
        next_node = tail.next
        tail.next = None
        reverse_list = reverse(cur)
        lp.next = reverse_list
        cur.next = next_node

        return dummy.next


        # # Iteration - II
        # # time: n
        # # space: 1
        # dummy = ListNode(0, head)
        # lp = dummy
        # for _ in range(left - 1):
        #     lp = lp.next
            
        # cur = lp.next
        # prev = None
        # for _ in range(right - left + 1):
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        
        # lp.next.next = cur
        # lp.next = prev

        # return dummy.next