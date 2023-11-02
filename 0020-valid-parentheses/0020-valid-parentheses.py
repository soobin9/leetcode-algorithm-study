class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                # pop할 값이 없다면 
                if len(stack) == 0:
                    return False 
                
                t = stack.pop()
                if c == ')' and t != '(':
                    return False 
                elif c == '}' and t != '{':
                    return False 
                elif c == ']' and t != '[':
                    return False 
        
        # 모두다 pop 되어있다면 
        if len(stack) == 0:
            return True 
        
        return False
            