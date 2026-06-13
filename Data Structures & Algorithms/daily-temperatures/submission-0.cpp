class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        int count = 0;
        int n = temp.size();
        vector<int> res(n, 0);
        stack<int> stk;

        for(int i = 0; i < n;i++){
            while(!stk.empty() && temp[i] > temp[stk.top()]){
                int prevDay = stk.top();
                stk.pop();
                res[prevDay] = i - prevDay;
            }
            stk.push(i);
        }
        return res;

        // int count = 0;
        // int n = temp.size();
        // vector<int> res(n, 0);

        // for(int i=0;i<n;i++){
        //     for(int j = i+1; j<n; j++){
        //         if(temp[i] < temp[j]){
        //             count = j - i;
        //             break;
        //         }
        //     }
        //     res[i] = count;
        //     count = 0;
        // }
        // return res;
    }
};
