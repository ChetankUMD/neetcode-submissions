# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getkth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            prev, cur = kth.next, group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next

    def getkth(self, ls, k):
        while ls and k > 0:
            ls = ls.next
            k -= 1
        return ls