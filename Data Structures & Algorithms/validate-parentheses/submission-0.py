class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                   return false
                stack.pop()
            else:
                stack.append(char)               
        return not stack        