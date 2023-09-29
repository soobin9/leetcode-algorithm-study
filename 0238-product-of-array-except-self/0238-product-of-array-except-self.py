class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 1st try - time limit 
        # results = [1 for _ in range(len(nums))]
        # for i, n in enumerate(nums):
        #     for j, n in enumerate(nums):
        #         if j != i :
        #             results[i] = results[i] * n
                    
        # 2nd try
#         v = 1 
#         for n in nums:
#             v = v * n 
        
#         results = [1 for _ in range(len(nums))]
#         for i, n in enumerate(nums):
#             # 0인 경우에는 예외 처리 
#             if n != 0 :
#                 results[i] = v / n 
#             else:
#                 for j, n in enumerate(nums):
#                     if j != i :
#                         results[i] = results[i] * n
        
        # 3rd try - youtube - https://www.youtube.com/watch?v=bNvIQI2wAjk
        # 앞에서부터 곱한 값 
        prev = [1 for _ in range(len(nums) + 1)]
        p = 1 
        for i, n in enumerate(nums):
            prev[i + 1] = p * n 
            p = prev[i + 1]
        
        # 뒤에서부터 곱한 값 
        suff = [1 for _ in range(len(nums) + 1)]
        s = 1 
        for i, n in enumerate(nums[::-1]):
            suff[i + 1] = s * n 
            s = suff[i + 1]
            
        results = []
        for i, n in enumerate(nums):
            results.append(prev[i] * suff[len(nums) - i - 1])
        
            
        return results