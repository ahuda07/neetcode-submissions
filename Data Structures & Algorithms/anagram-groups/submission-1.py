class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = dict()
        for i in strs:
            key = tuple(sorted(i))
            if key not in grouped:
                grouped[key] = [i]
            else:
                grouped[key].append(i)
        return list(grouped.values())
            