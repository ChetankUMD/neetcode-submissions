class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> cur;
        backtrack(0, nums, cur, res);
        return res;
    }

private:
    void backtrack(int i, vector<int>& nums, vector<int>& cur, vector<vector<int>>& res){
        if(i >=nums.size()){
            res.push_back(cur);
            return;
        }
        cur.push_back(nums[i]);
        backtrack(i+1, nums, cur, res);
        cur.pop_back();
        backtrack(i+1, nums, cur, res);
    }
};
