class Solution:
    def canJump(self, nums) -> bool:
        c = 0
        for i in nums:
            if c < 0:
                return False
            elif i > c:
                c = i
            c -= 1
            
        return True