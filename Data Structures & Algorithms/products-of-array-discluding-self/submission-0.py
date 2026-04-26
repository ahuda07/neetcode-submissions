class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this is an array or hashing problem
        # most likely a o(n) or o(n log n) solution
        # this might be a two pointer technique problem
        # i think maybe i can have a prev pointer + next pointer
            # set prev to current and current to next
            # repeat?
        products = []
        product = 1
        for i in range(len(nums)):
            products.append(product)
            product = nums[i] * product
        product = 1
        for k in range(len(nums) - 1, -1, -1):
            products[k] = products[k] * product
            product = product * nums[k]
        return products
        