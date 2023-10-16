class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        result = 0 
        prev = None
        tempCount = 1
        
        nums.sort()
        for n in nums:
            # prev 이 초기화되어있거나 전 값과 동일한 경우 
            if prev == None or prev == n:
                prev = n
            # 연속된 경우 
            elif prev + 1 == n:
                prev = n 
                tempCount += 1 # 연속적인 경우 카운트 
            else:
                prev = n # 초기화 
                tempCount = 1
                
            result = max(result, tempCount) # 값 갱신 
      
        
        return result