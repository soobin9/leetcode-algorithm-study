class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        dset = defaultdict(list)
        for i, num in enumerate(nums):
            dset[num].append(i)
        
        result = set()
            
        # 시간 줄이기 위해 체크한 값에 대해서 결과값 저장 
        checked = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                check = nums[i] + nums[j] 

                if (nums[i], nums[j]) in checked:
                   continue
        
                if -check in dset:
                    # i,j 조건 확인 
                    if dset[-check] == [i] or dset[-check] == [j] or dset[-check] == [i,j] or dset[-check] == [j, j]:
                        continue
                    
                    # 중복값 체크 위해 정렬해서 키를 생성 
                    r = tuple(sorted([nums[i], nums[j], -check]))
                    result.add(r)

                # 시간 초과 해결하기 위해 저장해둠 
                checked.add((nums[i], nums[j]))
                
        
        return result