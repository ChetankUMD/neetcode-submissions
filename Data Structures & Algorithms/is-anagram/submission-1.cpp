class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sm;
        // unordered_map<char, int> tm;
        if(s.length() != t.length()) return false;
        for(int i = 0; i<s.length();i++){
            sm[s[i]]++;
            sm[t[i]]--;
        }
        for(auto se : sm){
            if(se.second != 0){
                return false;
            }
        }
        return true;
    }
};
