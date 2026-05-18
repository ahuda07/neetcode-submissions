class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = new Map();
        for(let i = 0; i < nums.length; i++){
            let compliment = target - nums[i];
            if(!seen.has(compliment)){
               seen.set(nums[i],i); 
            }else{
                return([seen.get(compliment),i]);
                }
            }
        }
    }

