class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, vector<int>>> distance;
        vector<vector<int>> res;

        for(int i = 0; i < points.size(); i++){
            double dis = points[i][0] * points[i][0] + points[i][1]*points[i][1];
            distance.push({dis, points[i]});
            if(distance.size() > k) { distance.pop();}
        }

        for(int i = 0;i<k;i++){
            auto r = distance.top();
            res.push_back(r.second);
            distance.pop();
        }

        return res;
    }
};
