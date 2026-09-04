from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        reference  = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = deque()
        
        for i in range(len(s)):
            if s[i] not in reference:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif reference[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0  

        
        




































        