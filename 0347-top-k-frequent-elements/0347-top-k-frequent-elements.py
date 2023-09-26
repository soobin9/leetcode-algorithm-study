class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        checks = dict()
        for num in nums:
            if num in checks:
                checks[num] = checks[num] + 1
            else:
                checks[num] = 1 
        
        # 빈도수로 정렬 
        print(checks.items())
        checks = sorted(checks.items(), key=lambda item: item[1], reverse=True )
        
        result = []
        for i, num in enumerate(checks):
            if i < k:
                result.append(checks[i][0])
        return result