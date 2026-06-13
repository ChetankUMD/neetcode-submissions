class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        int j =0,k=0;
        sort(nums.begin(),nums.end());
        set<vector<int>> res;
        for (int i=0;i<n;i++){
            for(int j =i+1;j<n;j++){
                for(int k = j+1;k<n;k++){
                    if(nums[i]+nums[j]+nums[k]==0){
                        res.insert({nums[i],nums[j],nums[k]});
                    }
                }
            }
            // j = i+1;
            // k = j+1;
            // while(j<n-1){
            //     k = j+1;
            //     while(k<n){
            //         if(nums[i]+nums[j]+nums[k]==0){
            //             cout << nums[i] << nums[j] << nums[k]<< endl;
            //             res.push_back({nums[i],nums[j], nums[k]});
            //         }
            //         k++;
            //     }
            //     j++;
            // }
            // return res;
        }
        return vector<vector<int>>(res.begin(),res.end());
    }
};
