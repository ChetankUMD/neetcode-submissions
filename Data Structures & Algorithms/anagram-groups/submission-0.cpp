class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> res;

        for (const auto& s : strs){
            std::vector<int> count(26,0);
            for (char c : s){
                count[c - 'a']++;
            }
            std::string key = std::to_string(count[0]);
            for (int i =1; i<26;i++){
                key += ',' + std::to_string(count[i]);
            }
            res[key].push_back(s);
        }
        std::vector<std::vector<std::string>> result;
        for(const auto& pair :res){
            result.push_back(pair.second);
        }
        return result;
    }
};
