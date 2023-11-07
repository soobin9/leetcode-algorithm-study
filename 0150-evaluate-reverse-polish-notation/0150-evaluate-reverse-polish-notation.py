class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
#         stack = [] 
#         for t in tokens:
#             if t not in ['/', '+', '-', '*']:
#                 stack.append(t)
#             else : 
#                 n1 = int(stack.pop())
#                 n2 = int(stack.pop())
                
#                 if t == '/':
#                     check = math.trunc(float(n2) / float(n1))
#                     stack.append(check)
#                 elif t == '+':
#                     stack.append(n2+n1)
#                 elif t == '-':
#                     stack.append(n2-n1)
#                 elif t == '*':
#                     stack.append(n2*n1)
#             # print(stack)
        
#         return int(stack.pop())

        stack = [] 
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
    
        return stack[0]
        