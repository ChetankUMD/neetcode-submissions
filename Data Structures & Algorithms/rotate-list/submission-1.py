# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        p = head
        dummy = ListNode(0)
        while p:
            p = p.next
            n+=1
        if n==0:
            return None
        k = k%n
        print(k)
        n1 = n-k-1
        p = head
        while n1>0:
            p = p.next
            n1-=1
        l1 = p.next
        p.next = None
        q=dummy
        q.next = l1
        prev = None
        l2 = q
        while l2:
            prev = l2
            l2 = l2.next
        
        prev.next = head

              

        return dummy.next