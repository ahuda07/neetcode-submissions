class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        checked = False
        for i in range(len(nums)):
            if nums[i] in seen:
                checked = True
                break
            else:
                seen.append(nums[i])
        return checked
