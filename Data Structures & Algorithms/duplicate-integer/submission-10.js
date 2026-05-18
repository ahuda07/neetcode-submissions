class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = new Map();
        for(const num of nums){
            if(!seen.has(num)){
                seen.set(num, 1);
            }else{
                seen.set(num, seen.get(num)+1);
            }
        }
        for(const value of seen.values()){
            if(value > 1){
                return true;
            }
        }
        return false;
    }
}
