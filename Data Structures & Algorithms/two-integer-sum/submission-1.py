class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in index:
                return [index[answer],i]
            else:
                index[nums[i]] = i
