class Solution(object):
    def isPalindrome(self, s):
        
        testString = [] 
        for c in s:
            if c.isalnum():
                testString.append(c.lower())
        
        for i,c in enumerate(testString):
            if c != testString[-i-1]:
                return False
        
        return True
        