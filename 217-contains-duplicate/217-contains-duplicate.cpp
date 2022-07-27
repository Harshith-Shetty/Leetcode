class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> temp;
        for(int i=0; i<nums.size(); i++) {
            temp.insert(nums[i]);
        }
        
        return ( temp.size() < nums.size() ) ? true : false;
    }
};