class Solution(object):
    def isPalindrome(self, s):
        
        # 1nd 
#         testString = [] 
#         for c in s:
#             if c.isalnum():
#                 testString.append(c.lower())
        
#         for i,c in enumerate(testString):
#             if c != testString[-i-1]:
#                 return False
            
        # 2st 
        newStr = "" 
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        
        
        return True
        