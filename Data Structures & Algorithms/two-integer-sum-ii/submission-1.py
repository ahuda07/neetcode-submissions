class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start with left and right 
        # while the left is bigger than the right
        # check if the two added together is the target, if not check if current is bigger
        # smaller -> left+1, right -> right-1

        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1,right + 1]
            elif curr < target:
                left += 1
            else:
                right -= 1
            