class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false;
        }
        const seen = new Map();
        for(const char of s){
            if(!seen.has(char)){
                seen.set(char, 1);
            }else{
                seen.set(char, (seen.get(char) || 0)+1)
            }
        }
        for(const char of t){
            if(seen.has(char)){
                seen.set(char, seen.get(char) - 1);
            }else{
                return false;
            }
        }
        for(const val of seen.values()){
            if(val !== 0){
                return false;
            }
        }
        return true;
    }
}
