class Solution:
    def majorityElement(self, nums) -> int:
        d={}
        n=len(nums)
        for i in nums:
            d.setdefault(i,0)
            d[i]+=1
            if d[i]>n//2:
                return i
        