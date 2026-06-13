class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(candidates.begin(), candidates.end());
        dfs(0, res, cur, candidates, target);
        return res;

    }

private:
    void dfs(int i, vector<vector<int>>& res, vector<int> cur, vector<int>& nums, int target){
        int sum =0;
        for(int c : cur){
            sum += c;
        }
        if(sum == target){
            res.push_back(cur);
            return;
        }
        if(i >= nums.size() || sum > target) return;
        
        cur.push_back(nums[i]);
        dfs(i+1, res, cur, nums, target);
        cur.pop_back();
        while(i+1 < nums.size() && nums[i] == nums[i+1]){
            i++;
        }
        dfs(i+1, res, cur, nums, target);
    }
};
