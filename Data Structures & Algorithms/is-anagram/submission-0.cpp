class Solution {
public:
    bool isAnagram(string s, string t) {
        // int flag = 0;
    // for(int i = 0; i<s.length(); i++){
    //     flag = 0;
    //     for(int j = 0; j<t.length(); j++){
    //         if(s[i]==t[j]){
    //             t[j]=0;
    //             flag =1;
    //             break;
    //         }
    //     }
    //     if(flag == 0){
    //         return false;
    //     }
    // }
    // for(int j = 0; j<t.length(); j++){
    //     if(t[j]!=0){
    //         return false;
    //     }
    // }
    // return true;

    // if (s.length() != t.length()){
    //     return false;
    // }

    // std::string sorts = s;
    // std::string sortt = t;

    // std::sort(sorts.begin(), sorts.end());
    // std::sort(sortt.begin(), sortt.end());

    // return sorts==sortt;

    if (s.length() != t.length()){
        return false;
    }

    std::vector<int> frequency(256, 0);

    for(size_t i =0; i<s.length(); i++){
        ++frequency[s[i]];
        --frequency[t[i]];
    }

    for( int count : frequency){
        if (count != 0){
            return false;
        }
    }
    return true;
    }
};
