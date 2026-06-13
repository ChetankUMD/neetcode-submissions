class TrieNode{
public:
    unordered_map<char, TrieNode*> children;
    bool end = false;
};


class Solution {
    private:
    bool search(string word, TrieNode* root) {
        auto p = root;
        for(auto c : word){
            if(p->children.find(c) == p->children.end()){
                return false;
            }
            p = p->children[c];
        }
        return true;
    }
    void insert(TrieNode* root, string& word){
        TrieNode* p = root;
        for(char c : word){
            if(!p->children.count(c)){
                p->children[c] = new TrieNode();
            }
            p = p->children[c];
        }
    }

    void dfs(vector<vector<char>>& board, int x, int y, string path, set<pair<int,int>>& visited, TrieNode* root){
        int row = board.size(), cols = board[0].size();
        path += board[x][y];
        insert(root, path);
        visited.insert({x,y});

        vector<pair<int,int>> dir = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for(auto [dx, dy] : dir){
            int nx = x +dx, ny = y + dy;
            if(nx >= 0 && nx < row && ny >= 0 && ny < cols && !visited.count({nx, ny})){
                set<pair<int, int>> nextVisited = visited;
                dfs(board, nx, ny, path, nextVisited, root);
            }
        }
    }

    TrieNode* buildTrie(vector<vector<char>> board){
        TrieNode* root = new TrieNode();
        int row = board.size(), cols = board[0].size();
        for(int i =0; i<row; i++){
            for(int j =0;j<cols; j++){
                set<pair<int, int>> visited;
                dfs(board, i, j, "", visited, root);
            }
        }
        return root;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = buildTrie(board);
        vector<string> res;
        for(string word : words){
            if(search(word, root)){
                res.push_back(word);
            }
        }
        return res;
    }


};
