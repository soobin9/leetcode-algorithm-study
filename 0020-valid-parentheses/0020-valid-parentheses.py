class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
#         stack = []
#         for c in s:
#             if c in ['(', '{', '[']:
#                 stack.append(c)
#             elif c in [')', '}', ']']:
#                 # pop할 값이 없다면 
#                 if len(stack) == 0:
#                     return False 
                
#                 t = stack.pop()
#                 if c == ')' and t != '(':
#                     return False 
#                 elif c == '}' and t != '{':
#                     return False 
#                 elif c == ']' and t != '[':
#                     return False 
        
#         # 모두다 pop 되어있다면 
#         if len(stack) == 0:
#             return True 

        # 2nd 
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # 비어있으면 true 로 리턴 
        return True if not stack else False
        
        return False
            