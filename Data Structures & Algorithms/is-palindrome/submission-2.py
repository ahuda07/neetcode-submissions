class Solution:
    def isPalindrome(self, s: str) -> bool:
        # so what this question wants is to check if a string that is stripped of non alphanumeric chars and lowerccased
        # is the same backwards
        # so a question i have is can a string be empty? in this case that would be true
        # i am assuming that we need to strip the string and lowercase it before starting
        # based off the first example, a good way to approach this is implementing a two pointer solution
        # i would also need to use the strip() function
        # to solve this i would create two pointers, one at the beginning and one at the end using a while loop
        # the chars would constantly check eachother to make sure they are matching, and once the l pointer meets r 
        # pointer it would then return true
        # if at any point the chars dont match it returns false
        # if they are constant, the pointers will iterate and decrement
        # this solution would be o(1) space because it is not implementing a new data structure and o(n) time 
        # because it is iterating through a string with size n which will take n time
        #cleaned + stripped string
        s = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


            