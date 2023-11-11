class Solution(object):
    def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
        
#         stack = [0]
#         res = [0] * len(temperatures)
#         checked = 1 
        
#         while checked < len(temperatures):
#             while len(stack) > 0:
#                 if temperatures[checked] > temperatures[stack[-1]]:
#                     res[stack[-1]] = checked - stack[-1]
#                     stack.pop()
#                 else:
#                     break
            
#             stack.append(checked)
#             checked += 1
        
#         return res

          res = [0] * len(temperatures)
          stack = [] # pair [temp, index]

          for i,t in enumerate(temperatures):
                while stack and t > stack[-1][0]:
                    stackT, stackInd = stack.pop()
                    res[stackInd] = (i - stackInd)
                stack.append([t, i])     
          return res

            