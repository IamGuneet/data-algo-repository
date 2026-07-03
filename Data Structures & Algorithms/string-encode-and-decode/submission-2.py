class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s))+"#"+s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        op = []
        start = 0
        while start < len(s):
            j = start
            while s[j]!= '#' and s[j]!= "":
                j+=1
            print(s[start:j])
            l = int(s[start:j])
            
            start_string = j+1
            end_string = start_string + l

            op.append(s[start_string:end_string])
            start = end_string

        return op