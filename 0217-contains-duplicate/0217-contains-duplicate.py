class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        uniqueList = dict()
        for num in nums:
            if num in uniqueList:
                return True 
            else:
                uniqueList[num] = 'exists'

        return False