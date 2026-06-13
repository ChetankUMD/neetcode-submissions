class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(auto n : nums){
            if(seen.count(n)>0){
                return true;
            }
            seen.insert(n);
        }
        return false;
    }
};
