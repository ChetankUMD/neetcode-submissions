
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd part
        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        first, second = head, prev
        #mearge both parts
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
