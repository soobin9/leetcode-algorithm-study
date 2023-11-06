class MinStack(object):

#     def __init__(self):
#         self.minStack = [sys.maxsize] 
#         self.stack = [] 

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         if (self.minStack[-1] > val):
#             self.minStack.append(val)
#         else:
#             self.minStack.append(self.minStack[-1])
#         self.stack.append(val)
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.minStack[-1]
        
    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # minStack 값이 있을때만 
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()