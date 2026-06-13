class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        int l =0,r=0;
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        for(int i =0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            l = i+1, r = n-1;
            while(l < r) {
                int sum = nums[i]+nums[l] + nums[r];
                if (sum == 0) {
                    // Return 1-based indices
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back( nums[l]);
                    temp.push_back(nums[r]);
                    res.push_back(temp);
                    l++;
                    r--;
                    while(l<r && nums[l] == nums[l-1]){
                        l++;
                    }
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
        // set<vector<int>> res;
        // for (int i=0;i<n;i++){
        //     for(int j =i+1;j<n;j++){
        //         for(int k = j+1;k<n;k++){
        //             if(nums[i]+nums[j]+nums[k]==0){
        //                 res.insert({nums[i],nums[j],nums[k]});
        //             }
        //         }
        //     }
        // }
        // return vector<vector<int>>(res.begin(),res.end());

    }
};
