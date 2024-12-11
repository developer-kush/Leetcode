string preprocess(string s){
    string res = "#";
    for(char c : s){
        res += c;
        res += '#';
    }
    return res;
}

vector<int> manachers(string s){
    s = preprocess(s);
    int n = s.size();
    vector<int> res(n);
    int l = 0, r = 0, mir = 0; 
    for (int idx = 0; idx<s.size(); idx++){
        if (idx >= r || idx + res[2*mir - idx] >= r){
            mir = idx;
            r = max(r, idx);
            l = 2*idx - r;
            while (0<=l-1 && r+1<n && s[l-1] == s[r+1]){
                l--;
                r++;
            }
            res[idx] = r-idx;
        } else {
            int x = 2*mir - idx;
            res[idx] = res[x];
        }
    }

    return res;
}

class Solution {
public:
    string longestPalindrome(string s) {
        vector<int> res = manachers(s);
        int idx = max_element(res.begin(), res.end())-res.begin();
        int maxlen = idx + res[idx];
        int start = idx - res[idx];
        s = preprocess(s);
        string result = "";
        for (int i = start+1; i < maxlen; i+=2){
            result += s[i];
        }
        return result;
    }
};