class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # num 별 count  
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n,c in count.items():
            freq[c].append(n)
            
        res = []
        
        # 뒤에서부터 시작 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
                    
        # O(n) -> bucket sort 
            
        
        print(count)