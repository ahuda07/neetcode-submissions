class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        checked = False
        for i in range(len(nums)):
            if nums[i] in seen:
                checked = True
                break
            else:
                seen.add(nums[i])
        return checked
