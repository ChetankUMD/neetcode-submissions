class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        dfs(0, res, cur, nums, target);
        return res;
    }

private:
    void dfs(int i, vector<vector<int>>& res, vector<int>& cur, vector<int>& nums, int target){
        int sum = 0;
        for(int n : cur){
            sum += n;
        }
        if(i >= nums.size() || sum > target){ return ;}
        if(sum == target){
            res.push_back(cur);
            return;
        }
        cur.push_back(nums[i]);
        dfs(i, res, cur, nums, target);
        cur.pop_back();
        dfs(i+1, res, cur, nums, target);
    }
};
