from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        top = -1
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]== '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack[top] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[top] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack[top] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack)!=0:
            return False

        return True
