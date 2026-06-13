class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n= nums.size();
        int slow = nums[0], fast = nums[0];
        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];

            if(slow==fast){
                break;
            }
        }
        int slow2 = nums[0];

        while(slow!=slow2){
            slow = nums[slow];
            slow2 = nums[slow2];
        }

        return slow;
        // for(int i=0;i<n;i++){
        //     for(int j=i+1;j<n;j++){
        //         if(nums[i]==nums[j]){
        //             return nums[i];
        //         }
        //     }
        // }
        // return 0;
        // while(nums[slow] != nums[fast]){
        //     if(slow != fast){
        //         if(slow>=n){
        //             slow = 0;
        //         }
        //         if(fast>=n){
        //             fast = 0;
        //         }
        //     }
        //     slow++;
        //     fast += 2;
        // }
        // int slow2 = 0;
        // for(int i = 0; i<n;i++){
        //     if(nums[slow] == nums[i]);
        // }
        return nums[slow];
    }
};