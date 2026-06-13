class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> que;

        for(int i = 0;i<nums.size();i++){
            int num = nums[i];

            while(!que.empty() && que.back() < num){
                que.pop_back();
            }
            que.push_back(num);

            if(i>=k && nums[i-k] == que.front()){
                que.pop_front();
            }

            if(i >= k -1){
                res.push_back(que.front());
            }

            
        }
        return res;




        // vector<int> res;
        // int l =0;
        // pair<int, int> longest = {0, INT_MAX};
        // bool flag = true;

        // for(int r = k-1; r < nums.size();r++){
        //     if(flag){
        //         longest.second = INT_MIN;
        //         for(l = r-k+1; l<=r;l++){
        //             if(longest.second<nums[l]){
        //                 longest.second = nums[l];
        //                 longest.first = l;
        //             }
        //         }
        //         res.push_back(longest.second);
        //         if(longest.first != r-k+1){
        //             flag = false;
        //         }
        //     }
        //     else{
        //         if(longest.second < nums[r]){
        //             longest.second = nums[r];
        //             longest.first = r;
        //         }
        //         res.push_back(longest.second);
        //         if(longest.first != r-k+1){
        //             flag = false;
        //         }
        //         else{
        //             flag = true;
        //         }
        //     }
        // }

        // return res;


        // vector<int> res;
        // int l = 0;
        // int longest = INT_MIN;

        // for(int r = k-1; r<nums.size();r++){
        //     longest = INT_MIN;
        //     for(l = r-k+1; l<=r;l++){
        //         if(longest<nums[l]){
        //             longest = nums[l];
        //         }
        //     }
        //     res.push_back(longest);
        // }

        // return res;
    }
};