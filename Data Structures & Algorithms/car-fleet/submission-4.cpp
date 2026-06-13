class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        int n = position.size();
        // stack<double> st;
        vector<pair<int, double>> cars(n);

        for(int i =0; i< n; i++){
            double time = (double)(target - position[i])/speed[i];
            cars.push_back({position[i], time});
        }

        sort(cars.rbegin(), cars.rend());
        // st.push(cars[0].second);
        double top = cars[0].second;
        int fleet = 1;
        for(auto car : cars){
            cout << car.second << " ";
            if(car.second > top){
                top= car.second;
                fleet++;
                // st.push(car.second);
            }
        }
        return fleet;
    }
};
