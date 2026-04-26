class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        print("first",count)
        for letter in t:
            if letter in count:
                count[letter] -= 1
        print(len(count))
        print(count.values())
        return True if all(v == 0 for v in count.values()) else False

            