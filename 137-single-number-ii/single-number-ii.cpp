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

        long res = 0;
        for (int i = 31; i >= 0; i--){
            res = 2 * res + arr[i];
        }
        return res;

    }
};