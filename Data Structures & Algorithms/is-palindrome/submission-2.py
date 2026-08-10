class Solution:
    def isPalindrome(self, s: str) -> bool:
        normal_str = "".join(char.lower() for char in s if char.isalnum())
        
        return normal_str == normal_str[::-1]
        