class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.length();
        int i =0, j=n;
        while(i<j){
            while(i < j && !isalnum(s[j])){
                j--;
            }
            while(j > i && !isalnum(s[i])){
                i++;
            }
            cout << s[i]<<s[j] << endl;
            if(tolower(s[j]) != tolower(s[i])){
                return false;
            }
            i++; j--;
        }
        return true;
    }
};
