class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int, int> dic;
        for(int i : arr){
            dic[i] += 1;
        }
        vector<int> occurence;
        for (const auto& pair : dic) {
            occurence.push_back(pair.second);
        }
        set<int> mySet(occurence.begin(), occurence.end());
        return mySet.size()  == occurence.size();
        
    }
};