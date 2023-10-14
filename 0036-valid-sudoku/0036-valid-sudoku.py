class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # 가로줄 확인 
        for row in board : 
            checks = set()
            for w in row :
                if w != '.' and w in checks:
                    return False
                checks.add(w)
                
        # 세로줄 확인 
        for c in range(9) : 
            checks = set()
            for row in board:
                if row[c] != '.' and row[c] in checks:
                    return False
                checks.add(row[c])
        
                
        # 3 * 3 확인 : 중심 좌표 기준으로 확인 
        for x in range(1,8,3):
            for y in range(1,8,3) :
                checks = set() 
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if board[x + dx][y + dy] != '.' and  board[x + dx][y + dy] in checks:
                            return False
                        checks.add( board[x + dx][y + dy])
                
                
                
                
        
        return True