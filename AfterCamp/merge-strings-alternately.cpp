class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string newstr; 
        int l =0, r = 0;

        while (l < word1.length() && r < word2.length()){
            newstr += word1[l];
            newstr += word2[r];
            l++; r++;
        }
        if (l < word1.length() ){ 
            newstr += word1.substr(l, word1.length() -l);
        }
        if (l < word2.length() ){ 
            newstr += word2.substr(r, word2.length() -r);
        }

        return newstr;
        
    }
};