class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else: 
                freq[char] = 1
        for char in t:
            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    del freq[char]
            else:
                return False
        return len(freq) == 0
            