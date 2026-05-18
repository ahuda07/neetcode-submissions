class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        for(const char of s){
            if("{([".includes(char)){
                stack.push(char);
            }else{
                let topElement = stack[stack.length - 1];
                if(("}".includes(char) && "{".includes(topElement)) || 
                (")".includes(char) && "(".includes(topElement)) || 
                ("]".includes(char) && "[".includes(topElement))){
                    stack.pop(char)
                }else{
                    stack.push(char);
                }
            }
        }
        return(stack.length === 0);
    }
}
