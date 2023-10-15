class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # a를 1번만 바꾼다 
            t = t.replace(s[i], '', 1)
                   
        if t == '':
            return True
        else:
            return False