class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # 중도포기한 풀이 
#         limit = height[0]
#         start = 0 
#         trap = 0
#         for end in range(1, len(height) - 1):
#             h = height[end]
#             if h > limit:
#                 length = min(height[start], height[end])
#                 t = end - 1
#                 while t >= start:
#                     if length > height[t]:
#                         trap += (length - height[t])
#                     print('..', t, trap, length)
#                     t -= 1 
                
#                 # 다음 목록 조회 
#                 start = end + 1
#                 limit = height[start]
#             else : 
#                 # 다음 높이로 이동 
#                 limit = h
            
#             # print(end, trap)

        if not height:
            return 0 
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1 
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
    
        
        return res