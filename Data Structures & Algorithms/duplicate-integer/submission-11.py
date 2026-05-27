class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # so this question is asking to return true if the array contains any duplicate integers and false if it doesnt
        # based off the first example, 3 appears twice so it would be true
        # a question: can the array be empty?
        # a brute force solution would to make nums into a set and check the len of the two, if the same then false, else true
        # this would be idk the times but its just not optimal
        # another brute force is using a double for loop to check the current integer with every other integer, this would be o(n^2)
        # an optimal solution would be to implement a hashmap, keeping track of seen numbers already
        # this is an o(n) time and space, and hashmaps have o(1) lookup times, making it quick to check duplicates
        # to do this we create an empty hashmap, then iterate through the array, adding integers we have not seen and return false if we 
        # already seen it

        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = 1
        return False
            