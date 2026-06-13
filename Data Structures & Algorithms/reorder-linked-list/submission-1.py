
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        tail = head
        while tail and tail.next and tail.next.next:
            p = tail
            r = None
            while p.next:
                r = p
                p = p.next
            r.next = None
            p.next = tail.next
            tail.next = p
            tail =p.next
        
        return