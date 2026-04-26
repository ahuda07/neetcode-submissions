class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            key = sorted(word)
            key = "".join(key)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(word)
        return list(buckets.values())