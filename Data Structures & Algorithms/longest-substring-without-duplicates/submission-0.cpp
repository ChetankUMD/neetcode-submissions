class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        unordered_map<char, int> map;
        int longest = 0, l = 0;

        for(int r =0; r<n;r++){
            map[s[r]]++;
            while(map[s[r]]>1){
                map[s[l]]--;
                l++;
            }
            longest = max(longest, r-l+1);
        }
        
        return longest;
        
        
        
        // int n = s.length();
        // if (s.empty()) return 0;

        // unordered_map<char, int> lastSeen; // Stores the last seen index of each character
        // int l = 0, longest = 0;

        // for (int r = 0; r < n; r++) {
        //     // If character has been seen and is within the current substring, update `l`
        //     if (lastSeen.find(s[r]) != lastSeen.end() && lastSeen[s[r]] >= l) {
        //         l = lastSeen[s[r]] + 1; // Move `l` to exclude the previous occurrence
        //     }

        //     // Store/update last seen index of s[r]
        //     lastSeen[s[r]] = r;

        //     // Calculate longest substring length
        //     longest = max(longest, r - l + 1);
        // }

        // return longest;
        
        
        
        
        
        
        
        
        
        // int n = s.length();
        // if(s=="") return 0;
        // int l =0, r=0, longest = 0;
        // for(int i = 0 ; i<n;i++){
        //     r = i;
        //     for(int j= l ; j<r;j++){
        //         if(s[i] == s[j]){
        //             l = j +1;
        //             break;
        //         }
                
        //     }
        //     if(longest < r-l+1){
        //         cout << l << r << endl;
        //         longest = r-l+1;
        //     }
            
        // }
        // return longest;













        // if(s=="") return 0;
        // // if(s==" ") return 1;
        // stack<string> st;
        // string ss;
        // int res = 0;
        // for (auto cha : s){
        //     if(st.empty()){
        //         string ss = std::string() + cha;
        //         st.push(ss);
        //         continue;
        //     }
        //     string present_string = st.top();
        //     bool found = false;
        //     for(int i = 0; i<present_string.length(); i++){
        //         if(cha == present_string[i]){
        //             found = true;
        //             break;
        //         }
        //     }
        //     if(found){
        //         st.push(string(1,cha));
        //     }
        //     else{
        //         st.top() = st.top() + string(1,cha); 
        //     }
                 
        // }
        // while(!st.empty()){
        //     cout << st.top() << endl;
        //     if(st.top().length() > res) res = st.top().length();
        //     st.pop();
        // }

        // return res;
    }
};