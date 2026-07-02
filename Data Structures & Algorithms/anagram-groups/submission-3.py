class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for s in strs:
            key = "".join(x for x in sorted(s))
            lookup.setdefault(key,[]).append(s)
        print(lookup)
        return list(lookup.values())