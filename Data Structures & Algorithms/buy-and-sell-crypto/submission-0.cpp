class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxp = 0;
        int minp = INT_MAX;

        for(int i=0;i<prices.size();i++){
            if(prices[i]>minp){
                maxp = max(maxp, prices[i]-minp);
            }
            minp = min(minp, prices[i]);
        }

        return maxp;
 
 
 
 
 
 
        // int n = prices.size();
        // int i = 0, j = 1;
        // int maxp = 0;
        // if(n==1){
        //     return 0;
        // }
        // while(i<n){
        //     while(j<n && prices[i]<prices[j]){
        //         if(prices[i]<prices[j]){
        //             maxp = max(maxp, prices[j]-prices[i]);
        //         }
        //         j++;
        //     }
        //     i=j;
        //     j = i+1;
        // }
        // return maxp;
    }
};