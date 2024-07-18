class Solution:
    def removeDuplicates(self, nums) -> int:
        nums[:]=sorted(set(nums))
        return len(nums)