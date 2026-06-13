
class Node{
public:
    int val_node;
    int key_node;
    Node* next = NULL;
    Node* prev = NULL;
    Node(int k, int v) : key_node(k), val_node(v), next(NULL), prev(NULL) {}
};

class LRUCache {

private:
    int cap;
    unordered_map<int, Node*> map;
    Node* left;
    Node* right;

    // 
    void remove(Node* node){
        Node* prev = node->prev;
        Node* next = node-> next;
        prev->next = next;
        next->prev = prev;
    }

    // insert towards right
    void insert(Node* node){
        Node* mru = right->prev;
        mru->next = node;
        right->prev = node;
        node->next = right;
        node->prev = mru;
    }

public:
    LRUCache(int capacity) : cap(capacity){
        left = new Node(0,0);
        right = new Node(0,0);
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        if(map.find(key) != map.end()){
            Node* node = map[key];
            remove(node);
            insert(node);
            return node->val_node;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(map.find(key)!=map.end()){
            remove(map[key]);
        }
        map[key] = new Node(key, value);
        insert(map[key]);

        if(map.size() > cap){
            Node* lru = left->next;
            remove(lru);
            map.erase(lru->key_node);
            delete lru;
        }
    }

    ~LRUCache(){
        Node* curr = left;
        while(curr){
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
};
