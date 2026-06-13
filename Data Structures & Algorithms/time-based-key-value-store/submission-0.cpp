class TimeMap {
public:
    map<string, vector<pair<string, int>>> key_value;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        key_value[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if(key_value.find(key) == key_value.end() ) return "";
        // for (auto &keys : key_value){
        //     for (auto &pair : keys.second){
        //         cout << pair.first << endl;
        //     }
        // }
        
        
        return search(key_value[key], timestamp);
    }

    string search(vector<pair<string, int>>& list, int timestamp){
        int n = list.size();
        int l =0, h = n-1, mid= 0;
        while(l<=h){
            mid = l+(h-l)/2;
            if(timestamp == list[mid].second){
                return list[mid].first;
            }
            if(list[mid].second > timestamp){
                h = mid-1;
            }
            else{
                l = mid +1;
            }
        }
        return h >= 0 ? list[h].first : "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */