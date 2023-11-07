class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int zeros = 0;
    for (int i = 0; i < nums.size(); i++){
        if(nums[i] != 0 and nums[zeros] == 0){
            swap(nums[zeros], nums[i]);
            zeros ++;

        }
        if (nums[zeros]!= 0){
            zeros ++;
        }
    }
        
    }
};