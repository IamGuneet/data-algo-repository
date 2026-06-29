from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count= defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            # print(key)
            count[key].append(str)
            # print(count)
        top_k = sorted(count.items(), key = lambda x: x[1] )
        return list(count.values())
        