class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
        for char in t:
            if char in seen:
                seen[char] -= 1
            else:
                return False
        return all(v == 0 for v in seen.values())
