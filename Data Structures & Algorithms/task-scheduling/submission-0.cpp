class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        queue<pair<int, int>> q;
        priority_queue<int> max_heap;
        unordered_map<char, int> map;
        int time = 0;

        for(auto task : tasks){
            map[task]++;
        }

        for(auto m : map){
            if(m.second > 0){
                max_heap.push(m.second);
            }
            
        }

        while(max_heap.size() || !q.empty()){
            time++;
            if(max_heap.empty()){
                time = q.front().second;
            }else{
                int count = max_heap.top() - 1;
                max_heap.pop();
                if(count > 0){
                    q.push({count, time+n});
                }
            }
            if(!q.empty() && q.front().second == time){
                max_heap.push(q.front().first);
                q.pop();
            }
        }
        return time;
    }
};
