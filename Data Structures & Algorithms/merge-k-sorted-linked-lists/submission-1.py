# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        result = None
        
        while len(lists) > 1:
            mearged = []
            for i in range(0, len(lists), 2):
                ls1 = lists[i]
                ls2 = lists[i+1] if len(lists) > (i+1) else None
                result = self.mergeTwoLists(ls1, ls2)
                mearged.append(result)
            lists = mearged

        return lists[0]

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
        