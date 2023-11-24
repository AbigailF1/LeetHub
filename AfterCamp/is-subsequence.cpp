class Solution {
public:
    bool isSubsequence(string s, string t) {
        int l = 0, r = 0, n = s.length(), m = t.length();
        int count = 0;
        while ((l < n) && (r < m)){
            if (s[l] == t[r]){
                l++;
                r++;
                count++;
            }
            else{ r++;}
            
        }
        return count == n;
    }
};