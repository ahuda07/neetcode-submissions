class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # so im given an array of intgers called nums and a integer varaible target, what they want me to do is 
        # return the indieces i and j that equal to target
        # some questions i want to ask looking at this is can the list of nums be empty?
        # can there be duplicates? 
        # just by looking at this i think a brute force solution would be to check every pair with eachother and check
        # if it equal to target 
        # to do this i would implement a double for loop in which the indeci i checks with all other integers j in the array
        # and return the indece that sum to target, but this would be o(n^2) time and would take too long to check with other pairs
        # espeically givern a longer list
        # however i think a more optimized solution would be to implement a hashmap, because of quick lookup times and 
        # becuase we can keep track of variables we have already seen, the lookup time is o(1) and it would be o(n) time and space
        # to implement this i would:
        # create an empty hashmap
        # create a for loop iterating through the array
        # intialize a num_i_need variable current num - target = num_i_need
        # check to see if that number is in the seen dictionary
        # if not, it adds the current number to the dict
        # if it is, then it returns the indici of num_i_need
        # if there were no pairs at all that match to target, then it would just return an empty dictionary
        seen = dict()
        for i in range(len(nums)):
            num_i_need = target - nums[i]
            if num_i_need in seen:
                break
            else:
                seen[nums[i]] = i
        return [seen[num_i_need],i]
