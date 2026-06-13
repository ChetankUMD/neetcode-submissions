class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, mid = 0;
        int hi = *max_element(piles.begin(), piles.end());
        int res = hi;

        while(l<=hi){
            mid = (l + hi)/2;
            long long sum = 0;
            for(int pile: piles){
                sum = sum + ceil(static_cast<double>(pile) / mid);
            }
            if(sum <= h){
                res = mid;
                hi = mid -1;
            }
            else{
                l = mid +1;
            }
        }

        return res;
    }
};