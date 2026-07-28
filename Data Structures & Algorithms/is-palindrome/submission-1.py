class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_string = "".join(char.lower() for char in s if char.isalnum() )
        if normalized_string == normalized_string[::-1]:
            return True
        return False