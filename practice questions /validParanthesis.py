class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       brackets = {')':'(', ']':'[', '}':'{'}
       for char in s:
           if char in '({[':
               stack.append(char)
           if char in ')}]':
               if stack and brackets[char] == stack[-1]:
                   stack.pop()
               else:
                    return False
       return not stack
            