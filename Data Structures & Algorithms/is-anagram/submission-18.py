class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counted = {}
        for letter in s:
            if letter not in counted:
                counted[letter] = 1
            else:
                counted[letter] += 1
        for letter in t:
            if letter in counted:
                counted[letter] -= 1
        return all(v == 0 for v in counted.values())
