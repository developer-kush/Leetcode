class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int arr[33];
        memset(arr, 0, sizeof(arr));

        for (int num: nums){
            for (int pos = 0; pos <= 31; pos++){
                arr[pos] = (arr[pos]+(num&1))%3;
                num = num >> 1;
            }
        }

        int res = 0;
        for (int i = 31; i >= 0; i--){
            res = (res<<1) | (arr[i]);
        }
        return res;

    }
};