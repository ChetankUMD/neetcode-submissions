class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> res;
        std::unordered_map<int, int> count;
        std::vector<std::vector<int>> freq(nums.size()+1);

        for (int n :nums){
            count[n]++;
        }
        for(const auto& it : count){
            freq[it.second].push_back(it.first);
        }
        for (int i = freq.size()-1;i>0;--i){
            for (int n : freq[i]){
                res.push_back(n);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
