class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # 1st 
        # sortedStrs = []
        # for str in strs:
        #     # 돌면서 eat -> aet 알파벳순으로 정렬 
        #     sortedStrs.append((str, ''.join(sorted(str))))
            
        # # 동일한 것끼리 정렬 
        # sortedStrs.sort(key = lambda x:x[1])
        
        # results = [[sortedStrs[0][0]]]
        # # 동일한 것끼리 묶어주기 
        # for i in range(1, len(sortedStrs)):
        #     originalValue = sortedStrs[i][0]
        #     checkValue = sortedStrs[i][1]
            
        #     # 전에 값과 동일하다면, 전 배열에 넣어주고 
        #     if sortedStrs[i - 1][1] == checkValue:
        #         results[-1].append(originalValue)
        #     # 전에 값과 다르면, 새로운 배열에 추가 
        #     else:
        #         results.append([originalValue])



        # 2nd 23.10.23
        # 리스트를 값으로 갖는 딕셔너리를 생성하면, 딕셔너리에 키를 추가할 때 키가 존재하지 않으면 빈 리스트가 자동으로 생성
        results = defaultdict(list)
        for s in strs:
            count = [0] * 26          # 알파벳 만큼 만들기 
            for c in s:
                # 아스키 코드에서 'a'는 97이고, 'b'는 98, 'c'는 99, 이런 식으로 계속 증가
                count[ord(c) - ord('a')] += 1 
            
            # count 를 tuple 형태로 바꿔야 'unhashable type:list 안 발생함 '
            results[tuple(count)].append(s)
        
        return results.values()
        