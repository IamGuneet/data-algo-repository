class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base = {}
        con = {}
        for i in s:
            base[i] = base.get(i, 0) + 1
        
        for i in t:
            con[i] = con.get(i,0)+1
        if (base == con):
            return True
        return False