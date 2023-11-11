class Solution(object):
#     res = [] 
    
#     def dfs(self, current, n):
#         openCnt = current.count("(")
#         closeCnt = current.count(")")
        
#         if len(current) == 2 * n:
#             if openCnt == n and closeCnt == n:
#                 self.res.append(current)
#             return;
#         else:            
#             # close 갯수 < open 갯수 
#             if closeCnt <= openCnt:
#                 self.dfs(current + "(", n)
#                 self.dfs(current + ")", n)
    
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         self.res = [] # 테스트 케이스 전에 예전에 돌린 값 초기화 
#         self.dfs("(", n)
#         return self.res
        
        
        
    def generateParenthesis(self, n):
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open 
        # valid IIF open == closed == n 
        
        stack = [] 
        res = [] 
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res
                
            
            
            
        
        
        
        
        
        