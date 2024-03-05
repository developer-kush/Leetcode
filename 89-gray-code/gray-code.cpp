class Solution {
public:
    int getIndex(int l, int r, int x){
        int mid = l + ((r-l)>>1);
        if ((r-l) <= 1) return x;
        if (x<=mid) return getIndex(l, mid, x);
        else return getIndex(mid+1, r, r-x+mid+1);
    }
    vector<int> grayCode(int n) {
        int end_point = (1<<n) - 1;
        vector<int> res;
        for (int i = 0; i<end_point+1; i++){
            res.push_back(getIndex(0, end_point, i));
        }
        return res;
    }
};