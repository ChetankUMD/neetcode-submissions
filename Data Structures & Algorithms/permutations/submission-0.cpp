class Solution {
    vector<vector<int>> res;
public:
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> path;
        vector<bool> pick(nums.size(),false);
        dfs(path, nums, pick);
        return res;
    }

    void dfs(vector<int>& path, vector<int>& nums, vector<bool>& pick){
        if(path.size() == nums.size()){
            res.push_back(path);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(!pick[i]){
                path.push_back(nums[i]);
                pick[i] = true;
                dfs(path,nums,pick);
                path.pop_back();
                pick[i] = false;
            }
        }
        
        
    }
};
