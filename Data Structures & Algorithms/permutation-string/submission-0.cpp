class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        unordered_map<char, int> map1;
        unordered_map<char, int> map2;
        int l = 0, k=0;
        if(m>n) return false;
        for(int i=0;i<m;i++){
            map1[s1[i]]++;
        }
        for(int r=0;r<n;r++){
            map2[s2[r]]++;

            if(r>=m){
                if(map2[s2[r-m]] == 1){
                    map2.erase(s2[r-m]);
                }
                else{
                    map2[s2[r-m]]--;
                }
            }
            if(map1 == map2){
                return true;
            }
        }
        return false;
    }
};