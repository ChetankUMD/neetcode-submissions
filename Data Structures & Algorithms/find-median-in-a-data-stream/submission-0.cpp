class MedianFinder {
public:
    vector<int> nums;
    MedianFinder() {
        nums = {};
    }
    
    void addNum(int num) {
        nums.push_back(num);
    }
    
    double findMedian() {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        double res = 0;
        if(n%2 != 0){
            int id = n/2;
            res = nums[id];
        }
        else{
            res = (nums[n/2 - 1] + nums[n/2]) / 2.0;
        }
        return res;
    }
};
