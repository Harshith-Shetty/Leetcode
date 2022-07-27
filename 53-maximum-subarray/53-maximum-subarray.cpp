class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, maximum = nums[0];
        for(int num : nums){
            sum += num;
            maximum = max(maximum, sum);
            if(sum < 0)
                sum = 0;
        }
    
        return maximum;
    }
};