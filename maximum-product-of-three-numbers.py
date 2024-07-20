class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])