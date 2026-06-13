/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    unordered_map<Node*, Node*> ref;
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return nullptr;
        }
        return dfs(node);
    }

    Node* dfs(Node* node){
        if(ref.find(node) != ref.end()){
            return ref[node];
        }

        Node* copy = new Node(node->val);
        ref[node] = copy;
        for(Node* n : node->neighbors){
            copy->neighbors.push_back(dfs(n));
        }
        return copy;
    }
};









