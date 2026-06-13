class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if(m == 0) return false;
        int n = matrix[0].size();
        if(n==0) return false;


        int l = 0, h = m-1, mid = 0;
        while(l<=h){
            mid = l+(h-l)/2;
            if (matrix[mid][0] <= target && target <= matrix[mid][n - 1]) {
                break; // Found the row where the target might exist
            }
            if(matrix[mid][0] >target){
                h = mid - 1;
            }
            else{
                l = mid +1;
            }
        }

        if (h < 0) return false;
        l = 0;
        h = n-1;
        int i = mid;
        while(l<=h){
            mid = l+(h-l)/2;
            if(matrix[i][mid]==target){
                return true;
            }
            if(matrix[i][mid] > target){
                h = mid - 1;
            }
            else{
                l = mid +1;
            }
        }
        return false;
    }
};