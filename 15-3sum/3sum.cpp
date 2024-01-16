class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;

        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n; i++){
            int hi = n-1;
            int req = -1 * nums[i];
            for (int lo=i+1; lo<n; lo++){
                if (lo>=hi) break;
                while (lo<hi && nums[i]+nums[lo]+nums[hi]>0){
                    hi-=1;
                }
                if (lo >= hi) break;
                if (nums[i]+nums[lo]+nums[hi] == 0){
                    vector<int> group = {nums[i], nums[lo], nums[hi]};
                    sort(group.begin(), group.end());
                    res.insert(group);
                }
            }
        }

        vector<vector<int>> finalRes;

        for (vector<int> group: res){
            finalRes.push_back(group);
        }

        return finalRes;
    }
};