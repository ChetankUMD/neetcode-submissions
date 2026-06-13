/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // Node* res = new Node(0);
        // Node* copy = res;
        Node* p = head, *q = head;

        unordered_map<Node*, Node*> map;
        
        while(p){
            map[p] = new Node(p->val);
            p=p->next;
        }

        while(q){
            map[q]->next = map[q->next];
            map[q]->random = map[q->random];
            q=q->next;
        }
        return map[head];
        // do{
        //     q->next = new Node(q->val);
        //     q = q->next;
        //     q->next = p;
        //     // if(p&&p->next){
        //     //     p = p->next;
        //     // }
        //     p = p->next;
        //     q = q->next;
        // }while(p);
        // while(head){
        //     cout << head->val << endl;
        //     head = head->next;
        // }
        // return q;
    }
};