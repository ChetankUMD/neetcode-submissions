class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> min_heap;
        int res;
        for(auto n : nums){
            min_heap.push(n);
            if(min_heap.size() > k) {min_heap.pop(); }
        }
        res = min_heap.top();
        
        return res;
    }
};
