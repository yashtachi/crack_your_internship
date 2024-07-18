class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        nums1[m:]=nums2
        return nums1.sort()
                