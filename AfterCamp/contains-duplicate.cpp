class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> mySet(nums.begin(), nums.end());
        return mySet.size() != nums.size();
    }
};