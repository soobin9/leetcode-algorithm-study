class Solution(object):
    res = [] 
    
    def dfs(self, current, n):
        openCnt = current.count("(")
        closeCnt = current.count(")")
        
        if len(current) == 2 * n:
            if openCnt == n and closeCnt == n:
                self.res.append(current)
            return;
        else:            
            # close 갯수 < open 갯수 
            if closeCnt <= openCnt:
                self.dfs(current + "(", n)
                self.dfs(current + ")", n)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = [] # 테스트 케이스 전에 예전에 돌린 값 초기화 
        self.dfs("(", n)
        return self.res
        
        
        
        