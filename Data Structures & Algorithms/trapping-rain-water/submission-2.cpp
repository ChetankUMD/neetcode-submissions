class Solution {
public:
    int trap(vector<int>& height) {
        
        int n = height.size();
        int l =0, r = n-1;
        int leftmax = height[l];
        int rightmax = height[r];
        int res = 0;

        while(l<r){
            if(leftmax < rightmax){
                l++;
                leftmax = max(leftmax, height[l]);
                res += leftmax - height[l];
            }
            else{
                r--;
                rightmax = max(rightmax, height[r]);
                res += rightmax - height[r];
            }
        }
        return res;
        // vector<int> area(n,0);
        // int j =0, k=0;
        

        // for(int i =0 ; i<n-1;i++){
        //     j = i-1;
        //     k = i+1;
        //     int left_height = 0 , right_height = 0;
        //     while(j>=0){
        //         cout << height[j] << endl;
        //         left_height = max(height[j], left_height);
        //         j--;
        //     }
        //     while(k<n){
        //         right_height = max(height[k], right_height);
        //         k++;
        //     }
        //     int present_area = min(left_height, right_height) - height[i];
        //     // cout << "i "<<i << endl;
        //     // cout << "j "<< j << endl;
        //     // cout << "k "<< k << endl;
        //     // cout << left_height << endl;
        //     // cout << right_height << endl;
        //     // cout << present_area << endl;
        //     if(present_area > 0){
        //         area[i] = present_area;
        //     }
        // }
        // int sum =0;
        // for(auto a : area){
        //     // cout << a << endl;
        //     sum = sum +a;
        // }
        // // cout << sum;
        // return sum;
    }
};
