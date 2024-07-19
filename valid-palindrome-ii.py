class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left, right, count):
           if count > 1:
                return False
           while left < right:
               if s[left] == s[right]:
                   left += 1
                   right -= 1
               else:
                return ispalindrome(left + 1, right, count + 1) or ispalindrome(left, right - 1, count + 1)
           return True
       
        return ispalindrome(0, len(s) - 1, 0)