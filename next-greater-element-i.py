class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d={}
        l=[]
        for idx,i in enumerate(nums2):
            d.setdefault(i,idx)
        n=len(nums2)
        for i in nums1:
            t=-1
            for j in range(d[i],n):
                if nums2[j]>i:
                    t=nums2[j]
                    break
            l.append(t)
        return l