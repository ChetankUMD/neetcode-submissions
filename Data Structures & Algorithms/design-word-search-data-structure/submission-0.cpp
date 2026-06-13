class TrieNode{
public:
    unordered_map<int, TrieNode*> children;
    bool terminal = false;
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode;
    }
    
    void addWord(string word) {
        auto p = root;
        for(auto c : word){
            if(p->children.find(c) == p->children.end()){
                p->children[c] = new TrieNode;
            }
            p = p->children[c];
        }
        p->terminal = true;
    }
    
    bool search(string word) {
        return dfs(word, 0, root);
    }
private:
    bool dfs(string word, int j, TrieNode* root){
        TrieNode* p = root;
        for(int i = j; i<word.size(); i++){
            char c = word[i];
            if(c == '.'){
                for(auto& [key, child] : p->children){
                    if(child != NULL && dfs(word, i+1, child)){
                        return true;
                    }
                }
                return false;
            }
            else{
                if(p->children.find(c) == p->children.end()){
                    return false;
                }
            }
            p = p->children[c];
        }
        if(p->terminal == true){
            return true;
        }
        return false;
    }
};
