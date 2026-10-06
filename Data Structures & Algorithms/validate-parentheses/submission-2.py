class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_to_check = {')': '(',
                         ']': '[',
                         '}': '{'}

        for char in s:
            if char in char_to_check:
                if stack and stack[-1] == char_to_check[char]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(char)
            
        return True if len(stack) < 1 else False