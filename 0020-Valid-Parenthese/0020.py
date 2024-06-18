class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' and len(stack) > 0 and stack[len(stack) - 1] == '(':
                stack.pop()
            elif char == '}' and len(stack) > 0 and stack[len(stack) - 1] == '{':
                stack.pop()
            elif char == ']' and len(stack) > 0 and stack[len(stack) - 1] == '[':
                stack.pop()
            else: 
                return False
            
        return len(stack) == 0
            