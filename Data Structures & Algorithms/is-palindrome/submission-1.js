class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLowerCase().replace(/[^a-z0-9g]/g,"");
        // two pointer solution, left and right pointers
        let left = 0;
        let right = s.length - 1;
        while(left < right){
            if(s[left] === s[right]){
                left++;
                right--;
            }else{
                return false;
            }
        }
        return true;
    }
}
