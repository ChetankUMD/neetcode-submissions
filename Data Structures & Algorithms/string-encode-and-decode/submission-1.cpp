class Solution {
public:

    string encode(vector<string>& strs) {
       string res;

       for(auto s : strs){
            int size = s.length();
            string str_size = to_string(size);
            res.append(str_size+'#'+s);
       }
       return res;
    }

    vector<string> decode(string s) {
        string str;
        vector<string> res;
        int i =0;
        while(i<s.size()){
            int hash = s.find('#',i);
            int length = stoi(s.substr(i , hash - i));
            string str = s.substr(hash + 1,length);
            res.push_back(str);
            i = hash + 1 + length;
        }
        return res;

        // int count = 0;
        // for(int i=0; i<s.length();i++){
        //     if(s[i]=='#' && isdigit(s[i-1])){

        //         count = s[i-1] - '0';
        //         cout << count;
        //         for(;count+1>0;++i, count--){
        //             str += s[i];
        //         }
        //     }
        //     str.erase(0, 1);
        //     res.push_back(str);
        //     str = "";
        // }
        // res.erase(res.begin());
        // return res;

        // for(int i = 0; i< s.length();i++){
            
        //     if(s[i] == '#'){
        //         if (!str.empty() && str[0] == '#') {
        //         str.erase(0, 1);
        //     }
        //     res.push_back(str);
        //     str = "";
        //     }
        //     str += s[i];
        // }
        // return res;
    }
};
