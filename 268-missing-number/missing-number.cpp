class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int tot = 0, n = nums.size();
        for (auto val: nums) tot += val;
        return ((n*(n+1)) >> 1) - tot;
    }
};