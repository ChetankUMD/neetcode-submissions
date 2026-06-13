class Solution {
public:
    int findMin(vector<int>& nums) {
        // auto min =  std::min_element(nums.begin(), nums.end());
        // return *min;
        int n = nums.size();
        int l = 0, h =n-1, mid = 0;
        int lowest = INT_MAX;
        while(l<=h){
            mid = l+(h-l)/2;
            cout << nums[mid] << endl;

            lowest = min(lowest, nums[mid]);
            if(nums[mid]>nums[h]){
                l = mid + 1;
                // cout << l << endl;
            }
            else{
                h = mid -1;
            }
            // cout << l << endl;
        }
        return lowest;
    }
};