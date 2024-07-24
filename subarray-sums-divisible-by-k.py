from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        n=len(nums)
        p=0
        res=0
        d=defaultdict(int)
        d[0]=1
        for i in nums:
            p = (p + i%k + k)%k
            res+=d[p]
            d[p]+=1
        return res