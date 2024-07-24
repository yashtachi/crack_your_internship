class Solution:
    def minMoves2(self, nums) -> int:
        m=0
        nums.sort()
        n=len(nums)
        ele=nums[n//2]
        for i in nums:
            m+=abs(i-ele)
        return m