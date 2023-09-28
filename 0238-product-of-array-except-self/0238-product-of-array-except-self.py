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
        v = 1 
        for n in nums:
            v = v * n 
        
        results = [1 for _ in range(len(nums))]
        for i, n in enumerate(nums):
            # 0인 경우에는 예외 처리 
            if n != 0 :
                results[i] = v / n 
            else:
                for j, n in enumerate(nums):
                    if j != i :
                        results[i] = results[i] * n
        
                    
            
        return results