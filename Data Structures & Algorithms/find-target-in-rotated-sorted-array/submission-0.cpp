class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, h = n-1, mid = 0;
        while(l<=h){
            mid = l+(h-l)/2;
            // cout << nums[mid] << endl;
            if(target == nums[mid]){
                return mid;
            }
            else if(nums[l] <= nums[mid]){
                if(target <= nums[mid] && target >= nums[l]){
                    h = mid-1;
                }
                else{
                    l = mid +1;
                }
            }
            else{
                if(target >= nums[mid] && target <= nums[h]){
                    l = mid +1;
                }
                else{
                    h = mid -1;
                }
            }
            // cout << h << endl;
        }
        return -1;
    }
};