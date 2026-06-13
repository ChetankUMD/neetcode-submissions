class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(candidates.begin(), candidates.end());
        dfs(0, res, 0, cur, candidates, target);
        return res;

    }

private:
    void dfs(int idx, vector<vector<int>>& res, int sum, vector<int> cur, vector<int>& nums, int target){
        if(sum == target){
            res.push_back(cur);
            return;
        }
        for(int i =idx; i<nums.size(); i++){
            if(i>idx && nums[i] == nums[i -1]){
                continue;
            }
            if(sum + nums[i] > target){
                break;
            }
            cur.push_back(nums[i]);
            dfs(i+1, res, sum+nums[i],cur, nums,target);
            cur.pop_back();
        }
    }
};
