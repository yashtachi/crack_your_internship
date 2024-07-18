class Solution:
    def twoSum(self,nums,target:int):
        d={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in d:
                return [d[diff],i]
            d[n]=i