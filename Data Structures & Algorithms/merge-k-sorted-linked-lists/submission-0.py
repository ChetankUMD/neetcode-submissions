class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None

        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head = None
            dummy = ListNode()
            head = dummy
            p = list1
            q = list2
            while p and q:
                if p.val <= q.val:
                    dummy.next = p
                    p = p.next
                    dummy = dummy.next
                else:
                    dummy.next = q
                    q = q.next
                    dummy = dummy.next
            
            if p:
                dummy.next = p
            else:
                dummy.next = q
            

            return head.next
        
        for ls in lists:
            result = mergeTwoLists(self, result, ls)

        return result