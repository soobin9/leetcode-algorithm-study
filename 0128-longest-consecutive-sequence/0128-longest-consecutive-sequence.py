class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        # 1nd 
#         result = 0 
#         prev = None
#         tempCount = 1
        
#         nums.sort()
#         for n in nums:
#             # prev 이 초기화되어있거나 전 값과 동일한 경우 
#             if prev == None or prev == n:
#                 prev = n
#             # 연속된 경우 
#             elif prev + 1 == n:
#                 prev = n 
#                 tempCount += 1 # 연속적인 경우 카운트 
#             else:
#                 prev = n # 초기화 
#                 tempCount = 1
                
                
#             result = max(result, tempCount) # 값 갱신 
      
        
#         return result


        # 2st 
        longest = 0
        numSets = set(nums)
        for n in numSets:
            if n -1 in numSets:
                continue;
            else:
                t = n 
                tlengh = 1 
                while t + 1 in numSets:
                    tlengh += 1 
                    t = t + 1 
                    
                longest = max(tlengh, longest)
                
        return longest
                    