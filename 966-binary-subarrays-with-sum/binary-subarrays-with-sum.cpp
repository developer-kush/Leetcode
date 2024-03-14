class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, int> ctr;
        ctr[0] = -1;
        int res = 0, curr = 0;

        for (int i = 0; i < nums.size(); i++){
            if ( nums[i] == 1 ){
                curr += 1;
                ctr[curr] = i;
            }
            if (curr >= goal){
                int ptr = (curr - goal + 1);
                res += (ctr[ptr]-ctr[ptr-1]);
            }
            if (goal == 0) res += i;
        }

        return res;
    }
};