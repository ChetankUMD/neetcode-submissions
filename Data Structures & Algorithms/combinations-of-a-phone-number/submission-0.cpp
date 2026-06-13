class Solution { 
    unordered_map<char, string> map = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    vector<string> res;
public:
    vector<string> letterCombinations(string digits) {
        string path;
        if(digits.length() > 0){
            dfs(0, digits, path);
        }
        return res;
    }

    void dfs(int dig_i, string &digits, string path){
        if(dig_i == digits.length()){
            res.push_back(path);
            return;
        }
        string temp = map[digits[dig_i]];
        for(int i = 0; i<temp.length();i++){
            dfs(dig_i+1, digits, path+temp[i]);
        }
        return;
    }
};