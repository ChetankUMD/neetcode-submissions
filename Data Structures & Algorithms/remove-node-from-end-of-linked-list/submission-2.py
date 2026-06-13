# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count len LL
        count = 0
        p = head
        while p:
            count+=1
            p=p.next
        # travers to the length-n
        if n == count:
            return head.next
        i = count-n-1
        cur = head
        while i>0:
            cur = cur.next
            i-=1
        cur.next = cur.next.next

        return head