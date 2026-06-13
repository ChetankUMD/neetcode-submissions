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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, total = 0;
        ListNode* p = l1;
        ListNode* q = l2;
        ListNode* res = new ListNode(0);
        ListNode* r = res;

        while(p || q|| carry){
            total = carry;
            
            if(p){
                total += p->val;
                p = p->next;
            }
            if(q){
                total += q->val;
                q = q->next;
            }

            carry = total/10;
            total = total%10;
            r->next = new ListNode(total);
            r = r->next;
        }
        return res->next;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // string s1;
        // string s2;
        // ListNode* p = l1;
        // ListNode* q = l2;
        // ListNode* res = new ListNode(0);
        // ListNode* pt = res;

        // while(p){
        //     s1 = s1 + to_string(p->val);
        //     p = p->next;
        // }
        // while(q){
        //     s2 = s2 + to_string(q->val);
        //     q = q->next;
        // }
        // reverse(s1.begin(), s1.end());
        // reverse(s2.begin(), s2.end());

        // int i1 = stoi(s1);
        // int i2 = stoi(s2);
        // int add = i1+i2;

        // string ans = to_string(add);
        // reverse(ans.begin(), ans.end());

        // add = stoi(ans);

        // for(int i=0; i<ans.length(); i++){
        //     int num = ans[i] - '0';
        //     pt->next = new ListNode(num);
        //     pt = pt->next;
        // }
        // return res->next;
    }
};