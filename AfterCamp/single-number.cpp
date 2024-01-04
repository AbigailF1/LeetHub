class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map <int, int> dic;
        for (int i: nums){
            dic[i] += 1;
        }
        for(const auto &p : dic){
            if (p.second == 1){
                return p.first;   
            }
        }
        return 0;
    }
};