class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i<nums.size(); i++){
            int complement = target-nums[i];
            auto it = std::find(nums.begin()+i+1, nums.end(), complement);
            if (it!= nums.end()){
                return {i, static_cast<int>(std::distance(nums.begin(), it))};
            }
        }
        return {};
    }
};
