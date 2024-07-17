class Solution:
    def findDuplicate(self, nums) -> int:
        d={}
        for i in nums:
            if i in d:
                return i
            else:
                d[i]=1
                