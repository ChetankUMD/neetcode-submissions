class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> path;
        sort(nums.begin(), nums.end());
        dfs(0, res, path, nums);
        return res;
    }

    void dfs(int i, vector<vector<int>>& res, vector<int>& path, vector<int>& nums){
        if(i == nums.size()){
            res.push_back(path);
            return;
        }

        if(i>nums.size()) return;
        path.push_back(nums[i]);
        dfs(i+1, res, path, nums);
        path.pop_back();

        while(i+1<nums.size() && nums[i] == nums[i+1]){
            i++;
        }
        dfs(i+1, res, path, nums);
    }
};
