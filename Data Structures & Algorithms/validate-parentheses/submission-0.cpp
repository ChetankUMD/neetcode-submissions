class Solution {
public:
    bool isValid(string s) {
        stack<char> sta;
        if(s[0] == ')' || s[0] == ']' || s[0] == '}') return false;
        for(auto st :s ){
            if(st == '(' || st == '[' || st == '{'){
                sta.push(st);
            }else{
                if(sta.empty()) {
                    return false;
                }
                char re = sta.top();
                if(st == ')' && re == '('){
                    sta.pop();
                    continue;
                }
                else if(st == ']' && re == '['){
                    sta.pop();
                    continue;
                }
                else if(st == '}' && re == '{'){
                    sta.pop();
                }
                else return false;
            }
        }
        if(sta.empty()){
            return true;
        }
        return false;
    }
};
