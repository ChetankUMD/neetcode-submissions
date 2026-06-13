class TrieNode{
public: 
    unordered_map<char, TrieNode*> children;
    bool terminal = false; 
};



class PrefixTree {
    TrieNode* root;
public:
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        auto p = root;
        for(int i =0;i<word.size();i++){
            auto it = p->children.find(word[i]);
            if(it == p->children.end()){
                p->children[word[i]] = new TrieNode(); 
            }
            p = p->children[word[i]];
        }
        p->terminal = true;
    }
    
    bool search(string word) {
        auto p = root;
        for(auto c : word){
            if(p->children.find(c) == p->children.end()){
                return false;
            }
            p = p->children[c];
        }
        if(p->terminal == true){
            return true;
        }
        return false;
    }
    
    bool startsWith(string prefix) {
        auto p = root;
        for(auto c : prefix){
            if(p->children.find(c) == p->children.end()){
                return false;
            }
            p = p->children[c];
        }
        return true;
    }
};
