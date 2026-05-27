class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram is a string that cotnains exact same characters as another string
        # a common base case to do is check if both lengths of string are equal
        # a brute force solution would be to use a double for loop to keep counters on each character and check if each
        # char has a one to one counter part
        # a more optimal solution is to implement a hashmap solution that keeps track of each character
        # we would iterate through the first string and store the charcters and compare it to the second string
        # if a character is not seen, we add it, if it is then we add a counter += 1
        # when iterating through second string, we would decrement, the algorithm will prove they are anagrams
        # if the value of the keys are all 0, if not they are not an anagram
        # then we return a t/f if the values of the all keys in dicts are 0

        seen = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in t:
            if char in seen:
                seen[char] -= 1
            else:
                return False
        for value in seen.values():
            if value != 0:
                return False
        return True

            