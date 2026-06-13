/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* mid = head;
        ListNode* mid_prev = NULL;
        ListNode* fast =head;
        ListNode* first = head;
        ListNode *temp1=NULL, *temp2=NULL;
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;

        if (!head || !head->next || !head->next->next) return;

        // find middel part
        while(fast&&fast->next){
            mid_prev = mid;
            mid = mid->next;
            fast = fast->next->next;
        }
        mid_prev->next = NULL;

        // reverse 2nd ll
        ListNode* p = mid;
        ListNode* q = NULL;
        ListNode* r = NULL;
        while (p) {
            r = q;
            q = p;
            p = p->next;
            q->next = r;
        }
        mid = q;

        // mearge two alternatively
        first = head;
        while(first && mid){
            temp1 = first->next;
            temp2 = mid->next;
            first->next = mid;
            if (temp1) mid->next = temp1;
            first = temp1;
            mid = temp2;
        }
    }
};