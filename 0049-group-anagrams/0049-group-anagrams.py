class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStrs = []
        for str in strs:
            # 돌면서 eat -> aet 알파벳순으로 정렬 
            sortedStrs.append((str, ''.join(sorted(str))))
            
        # 동일한 것끼리 정렬 
        sortedStrs.sort(key = lambda x:x[1])
        
        results = [[sortedStrs[0][0]]]
        # 동일한 것끼리 묶어주기 
        for i in range(1, len(sortedStrs)):
            originalValue = sortedStrs[i][0]
            checkValue = sortedStrs[i][1]
            
            # 전에 값과 동일하다면, 전 배열에 넣어주고 
            if sortedStrs[i - 1][1] == checkValue:
                results[-1].append(originalValue)
            # 전에 값과 다르면, 새로운 배열에 추가 
            else:
                results.append([originalValue])
        return results
    
    