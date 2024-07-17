class Solution:
    def moveZeroes(self, nums) -> None:
        c=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[c]=nums[i]
                c+=1
        for i in range(c,n):
            nums[i]=0
        