class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height) - 1 
        area = - sys.maxsize
        
        while l < r :
            area = max(area, (r - l) * min(height[l], height[r]))

            # 높이가 큰쪽으로 이동 
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        
        # 시간 초과 
#         area = - sys.maxsize
#         for l in range(len(height)):
#             for r in range(l + 1, len(height)):
#                 area = max(area, (r - l) * min(height[l], height[r]))
                
        return area