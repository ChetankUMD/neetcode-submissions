class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        vector<int> res;
        int i =0, j = 0;
        while(i<n ){
            j = i+1;
            while(j<n){

                if(numbers[i] + numbers[j] == target){
                    return {i+1,j+1};
                }
                j++;
            }
            i++;
        }
        return {0,0};
    }
};
