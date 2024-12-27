class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size();
        int mv = values[0], mi = 0, mxsc = 0;
        for (int i = 1; i < n; i++){
            int curr = values[i] + mv - (mi) - (i-mi);
            mxsc = max(mxsc, curr);
            if (values[i]+i > mv){
                mv = values[i]+i;
                mi = i;
            }
        }
        return mxsc;
    }
};