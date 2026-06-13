class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> res;
        for(int i =0 ;i<n;i++){
            int second = target - nums[i];
            auto it = find(nums.begin(), nums.end(), second);
            if(it != nums.end() && it-nums.begin() != i){
                res.push_back(i);
                res.push_back(it-nums.begin());
                sort(res.begin(), res.end());
                return res;
            }
        }
        return res = {};
    }
};
