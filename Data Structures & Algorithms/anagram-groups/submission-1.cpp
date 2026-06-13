class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> res;
        for(int i = 0; i< strs.size(); i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            map[s].push_back(strs[i]);
        }

        for(auto st : map){
            res.push_back(st.second);
        }

        return res;
    }
};
