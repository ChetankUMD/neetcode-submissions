class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int longest =0, l=0;
        int maxfrq = 0;
        unordered_map<char, int> map;
        for(int r=0;r<n;r++){
            map[s[r]]++;
            maxfrq = max(maxfrq, map[s[r]]);
            cout << maxfrq << endl;
            while((r-l+1) - maxfrq> k){
                map[s[l]]--;
                l++;
            }
            longest = max(longest, r-l+1);
        }
        return longest;
    }
};