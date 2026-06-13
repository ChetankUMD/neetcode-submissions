class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.length();

        while(i<j){
            if(!isalnum(s[i])){
                i++;
                continue;
            }
            if(!isalnum(s[j])){
                j--;
                continue;
            }
            cout << s[i]  << "  " << s[j];
            if(tolower(s[i]) != tolower(s[j])){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};
