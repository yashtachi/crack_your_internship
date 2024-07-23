class Solution:
    def countBits(self, n: int):
        l=[0]*(n+1)
        for i in range(n+1):
            l[i]=bin(i)[2:].count('1')
        return l