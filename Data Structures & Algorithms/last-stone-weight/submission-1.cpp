class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxheap;

        for(auto st : stones){
            maxheap.push(st);
        }
        int res;
        while(maxheap.size() > 1){
            int st1 = maxheap.top();
            maxheap.pop();
            int st2 = maxheap.top();
            maxheap.pop();
            res = abs(st1-st2);

            if(res == 0){
                continue;
            }
            else{
                maxheap.push(res);
            }
        }
        if(maxheap.empty()) return 0;
        return maxheap.top();
    }
};
