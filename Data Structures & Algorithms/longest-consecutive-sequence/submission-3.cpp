class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if(nums.size() == 0 ) return 0;
        int count = 1, res = 1;
        for(int i = 0;i<nums.size();i++){
            if(nums[i] == nums[i+1]){
                continue;
            }
            else if(nums[i]+1 == nums[i+1]){
                count++;
                res = max(res, count);
            }
            else{
                count = 1;
            }
        }

        return res;
    }
};
