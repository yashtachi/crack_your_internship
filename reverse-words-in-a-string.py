class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l=l[::-1]
        return ' '.join(l)