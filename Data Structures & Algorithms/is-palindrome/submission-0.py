class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        cleaned = [char.lower() for char in s if char.isalnum()]
        start = 0
        end = len(cleaned)-1

        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start+=1
            end -=1
        return flag
        