
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs) ==1:
            # return list(strs)
        map_anagrams = {}
        op = []
        for string in strs:
            ordered_str = "".join(sorted(string))
            if ordered_str not in map_anagrams:
                map_anagrams[ordered_str] = []
            map_anagrams[ordered_str].append(string)
        # print(map_anagrams)
        for x in map_anagrams.values():
            op.append(x)
        return op     