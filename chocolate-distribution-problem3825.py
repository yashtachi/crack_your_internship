class Solution:

    def findMinDiff(self, A,n,m):
        A.sort()
        ans=float('inf')
        ans=min(ans,A[m-1]-A[0])
        i=1
        while i+m-1<n:
            ans=min(ans,A[i+m-1]-A[i])
            i+=1
        return ans