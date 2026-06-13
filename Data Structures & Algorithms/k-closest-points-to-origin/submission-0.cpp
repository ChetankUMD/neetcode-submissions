class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, vector<int>>, vector<pair<double, vector<int>>> , greater<pair<double, vector<int>>>> distance;
        vector<vector<int>> res;

        for(int i = 0; i < points.size(); i++){
            double dis = sqrt(pow(0 - points[i][0], 2)+ pow(0 - points[i][1], 2));
            distance.push({dis, points[i]});
        }

        for(int i = 0;i<k;i++){
            auto r = distance.top();
            res.push_back(r.second);
            distance.pop();
        }

        return res;
    }
};
