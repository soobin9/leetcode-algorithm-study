class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = [] 
        for t in tokens:
            if t not in ['/', '+', '-', '*']:
                stack.append(t)
            else : 
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                
                if t == '/':
                    check = math.trunc(float(n2) / float(n1))
                    stack.append(check)
                elif t == '+':
                    stack.append(n2+n1)
                elif t == '-':
                    stack.append(n2-n1)
                elif t == '*':
                    stack.append(n2*n1)
            # print(stack)
        
        return int(stack.pop())
        