class Solution:
    def threeSum(self, nums):
        l=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if  i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,n-1
            while j<k:
                t=nums[i]+nums[j]+nums[k]
                if t==0:
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif t>0:
                    k-=1
                else:
                    j+=1
        return l  