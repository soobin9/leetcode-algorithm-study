class Solution(object):
    def isPalindrome(self, s):
        
        stack = [] 
        for c in s:
            if c.isalnum():
                stack.append(c.lower())
        
        for i,c in enumerate(stack):
            if c != stack[-i-1]:
                return False
        
        return True
        