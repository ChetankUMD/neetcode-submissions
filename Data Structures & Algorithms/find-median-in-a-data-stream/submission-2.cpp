class MedianFinder {
public:
    priority_queue<int> max;
    priority_queue<int, vector<int>, greater<int>> min;
    MedianFinder() {
    }
    
    void addNum(int num) {
        max.push(num);
        if(!min.empty() && min.top() < max.top()){
            min.push(max.top());
            max.pop();
        }


        if(max.size() > min.size() + 1){
            int temp = max.top();
            max.pop();
            min.push(temp);
        }
        if(min.size()>max.size()+1){
            int temp = min.top();
            min.pop();
            max.push(temp);
        }
    }
    
    double findMedian() {
        int maxn = max.size();
        int minn = min.size();

        if(maxn == minn){
            return (max.top() + min.top()) /2.0;
        }else if(maxn> minn){
            return max.top();
        }
        else{
            return min.top();
        }
        return -1;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // sort(nums.begin(), nums.end());
        // int n = nums.size();
        // double res = 0;
        // if(n%2 != 0){
        //     int id = n/2;
        //     res = nums[id];
        // }
        // else{
        //     res = (nums[n/2 - 1] + nums[n/2]) / 2.0;
        // }
        // return res;
    }
};
