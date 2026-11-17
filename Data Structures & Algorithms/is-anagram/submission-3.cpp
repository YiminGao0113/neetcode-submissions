class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> dict1;
        unordered_map<char, int> dict2;
        
        for (auto ss : s){
            dict1[ss] += 1;
        }

        for (auto tt: t){
            dict2[tt] += 1;
        }

        for (int i = 0; i < s.size(); i++){
            if (dict1[s[i]] != dict2[s[i]]){
                return false;
            }
        }

        if (dict1.size()!= dict2.size()){
            return false;
        }
        
        return true;
    }
};
