class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int i =0, j= n-1, k =0;
        int res=0;

        while(i<j){
            int height = min(heights[i], heights[j]);
            int len = j-i;
            res = max(res, height*len);
            (heights[i]>=heights[j]) ? j-- : i++;
            // k =j;
            // while(k>i){
            //     int height = min(heights[i], heights[k]);
            //     int len = k-i;
            //     cout << height << len << endl;
            //     res = max(res, height*len);
            //     cout << res << endl;
            //     k--;
            // }
            // i++;
        }

        return res;
        
    }
};
