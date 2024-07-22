class Solution:
    def productExceptSelf(self, nums, n):
        r=[0]*(n)
        c=nums.count(0)
        if c>1:
            return r
        elif c==1: 
            p=1
            for i in nums:
                if i!=0:
                    p*=i
            for i in range(n):
                if nums[i]==0:
                    r[i]=p
                    break
            return r
        else:
            p=1
            for i in nums:
                p*=i
            for i in range(n):
                r[i]=p//nums[i]
            return r