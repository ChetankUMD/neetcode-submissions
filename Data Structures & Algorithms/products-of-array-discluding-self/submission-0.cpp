class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);
        int final = 1;
        int flag = 0;
        int index = 0;
        int in = 0;
        // for(int i=0; i<n; i++){
        //     for (int j=0;j<n;j++){
        //         if(i!=j){
        //             result[i] = result[i] * nums[j];
        //         }
                
        //     }
        // }
        for(int num : nums){
            if(num != 0){
                final = final*num;
            }
            else{
                flag += 1;
                if(flag > 1){
                    result.assign(n,0);
                    return result;
                }
                in = index;
            }
            index++;
        }
        if(flag == 1){
            result.assign(n,0);
            result[in] = final;
            return result;
        }
        for (int i = 0; i< nums.size(); i++){
            
            if (nums[i] != 0){
                result[i] = final/nums[i];
            }
            
        }
        return result;
    }
};
