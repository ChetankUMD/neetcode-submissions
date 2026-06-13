class Solution {
    vector<vector<string>> res;
public:
    vector<vector<string>> partition(string s) {
        vector<string> path;
        dfs(0, s, path);
        return res;
    }

    void dfs(int ind, string &s, vector<string> &path){
        if(ind == s.length()){
            res.push_back(path);
            return;
        }
        for(int i=ind; i<s.length();i++){
            if(isPalindrome(s, ind, i)){
                path.push_back(s.substr(ind, i-ind+1));
                dfs(i+1, s, path);
                path.pop_back();
            }
        }
    }


    bool isPalindrome(string s, int start, int end) {
        while(start<end){
            if(s[start++] != s[end--]){
                return false;
            }
        }
        return true;
    }
};