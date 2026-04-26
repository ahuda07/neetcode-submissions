class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char
        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True



            