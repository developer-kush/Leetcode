class Solution {
public:
    vector<string> split(string s){
        vector<string> res;
        string curr = "";
        for (int i = 0; i<s.size(); i++){
            if (s[i]==' ') continue;
            while (s[i]!=' ' && i < s.size()){
                curr += s[i]; 
                i++;
            }
            res.push_back(curr);
            curr = "";
        }
        return res;
    }

    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> mp;
        unordered_map<string, char> backmap;

        vector<string> strings = split(s);

        if (pattern.size() != strings.size()) return false;

        for (int i = 0; i < pattern.size(); i++){
            if (mp.find(pattern[i]) == mp.end() && backmap.find(strings[i]) == backmap.end()){
                mp[pattern[i]] = strings[i];
                backmap[strings[i]] = pattern[i];
            } else if (
                (mp.find(pattern[i]) == mp.end() && backmap.find(strings[i]) != backmap.end()) ||
                (mp.find(pattern[i]) != mp.end() && backmap.find(strings[i]) == backmap.end())
            ) return false;
            else {
                if (mp[pattern[i]] != strings[i] || backmap[strings[i]] != pattern[i]) return false;
            }
        }

        return true;
    }
};